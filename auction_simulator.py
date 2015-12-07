#an auction simulator
#Sam Rossin
#fall 2015

import bidding_agent
import user_interface
import card
import random
import string
import os
import inspect
import importlib


NUM_ROUNDS = 10
STARTING_BUDGET = 1000
CARDS_PER_AGENT = 10

#scoring constants
DOMINATE_POINTS = 1
HIGHEST_POINTS = 1

#this is useful for printing stuff
CATAGORIES = ["Science", "Ecology", "Culture", "Commerce", "Industry"]





#finds all classes in the given directory that are subclasses
#of BiddingAgent
def get_agent_classes(directory = "agents"):
    modules = [file_name[:-3] for file_name in os.listdir(directory) if file_name.endswith('.py')]
    agent_classes = []
    for module_name in modules:
        module = importlib.import_module(directory + "." +  module_name)
        for name, agent in inspect.getmembers(module, inspect.isclass):
            if agent not in agent_classes and issubclass(agent, bidding_agent.BiddingAgent):
                if agent != bidding_agent.BiddingAgent:
                    agent_classes.append(agent)
    return agent_classes


#creates a bidding agent for each bidding agent class
#
#returns a list of these agents
#
#params: a list of classes, a list of cards, and a budget
#this id of an agent will be its position in the list
def make_bidding_agents(agent_classes, cards, budget):
    agents = []
    for i in range(len(agent_classes)):
        agents.append(agent_classes[i](cards, i, len(agent_classes), budget))
    return agents


#generates the cards for a round. this can be replaced with
#any scheme for generating cards, this randomizer is a place-holder
#it doesn't follow the reqiured rules or anything
def generate_cards(num, round_number):
    cards = []
    for i in range(num):
        name = "".join(random.choice(string.ascii_letters) for i in range(10)) 
        cards.append(card.Card(name, random.randint(0, 8), random.randint(0, 8),
                          random.randint(0, 8), random.randint(0, 8),
                          random.randint(0, 8)))
    return cards
    

#does a round of bids
#
#params: the round number, the card being bid on
def get_bids(card, index, agents, budgets, UI):
    UI.on_auction_started(card)
    bids = [];
    
    for i in range(len(agents)):
        bid = agents[i].getBid(card, index)
        
        if type(bid) != int:
            bid = 0
            UI.on_illegal_bid_received(i, "type")
        elif bid > budgets[i]:
            bid = 0
            UI.on_illegal_bid_received(i, "budget")
            
        UI.on_bid_received(card, i, bid)
        
        bids.append((i, bid))
    return bids
    

#gives out the results of a round of bids
#bids is a list of tuples, (id, bid)
def give_results(bids, agents, card, budgets, UI):
    bids = sorted(bids, key = lambda x: x[1], reverse = True)
    winner = bids[0][0]
    price = bids[1][1]
    
    #keep track of budgets
    budgets[winner] -= price
    
    #sort by agent
    bids = sorted(bids, key = lambda x: x[0])
    formatted_bids = [x[1] for x in bids]
    for agent in agents:
        agent.seeResults(card, winner, price, formatted_bids)
    
    UI.on_auction_finished(card, winner, price)
    return winner


#caculates everyones score
#params: dictionary of cards won, num agents
#return list of scores
#
#may need to reorganize this to work with vizualizations
def calculate_scores(cards_won, num_agents, UI):
    #total each players scores
    score = [0]*num_agents
    totals = []
    for i in range(num_agents):
        total = [0]*len(CATAGORIES)
        if i in cards_won:
            for card in cards_won[i]:
                for j in range(len(CATAGORIES)):
                    total[j] += card.getList()[j+1] 
        totals.append(total)
    
    #calculate domination scores
    dominations = []
    for i in range(num_agents):
        for j in range(i):
            iWins = 0
            jWins = 0
            for k in range(5):
                if totals[i][k] > totals[j][k]:
                    iWins += 1
                elif totals[i][k]<totals[j][k]:
                    jWins += 1
            if iWins > jWins:
                score[i] += DOMINATE_POINTS
                dominations.append((i, j))
            elif jWins > iWins:
                score[j] += DOMINATE_POINTS
                dominations.append((j, i))
                
    #calculate scores based on largest total
    catagories = [0]*len(CATAGORIES)
    for i in range(len(CATAGORIES)):
        highscore = -1
        high_id = -1
        for j in range(len(totals)):
            if (totals[j][i] > highscore):
                highscore = totals[j][i]
                high_id = j
        score[high_id] += HIGHEST_POINTS
        catagories[i] = high_id
        
    UI.on_round_finished(score, dominations, catagories)
    return score
                
            
            
def main():
    #build UI
    UI = user_interface.UserInterface()
    
    #set up game
    agent_classes = get_agent_classes()
    UI.on_agents_discovered([x.__name__ for x in agent_classes])
    num_agents = len(agent_classes)
    
    for rnd in range(NUM_ROUNDS):
        
        #set up round
        cards = generate_cards(num_agents*CARDS_PER_AGENT, rnd)
        UI.on_round_started(rnd, cards)
        
        agents = make_bidding_agents(agent_classes, cards, STARTING_BUDGET);
        budgets = [STARTING_BUDGET for agent in agents]
        cards_won = {}
        
        #do bidding
        for i in range(len(cards)):
            bids = get_bids(cards[i], i, agents, budgets, UI)
            winner = give_results(bids, agents, cards[i], budgets, UI)
            if winner in cards_won:
                cards_won[winner].append(cards[i])
            else:
                cards_won[winner] = [cards[i]]
        
        
        #do scoring
        calculate_scores(cards_won, num_agents, UI)
    
    UI.on_game_finished()
    

if __name__ == '__main__':
    main()