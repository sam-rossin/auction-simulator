#User Interface class
#Sam Rossin
#fall 2015

#User interface class. Should be rewritten to make the UI happen, with the same methods
#Current functions are stubs.
import auction_simulator

class UserInterface:
    #anything do initialize the UI should be here
    def __init__(self):
        self.agents = None
    
    #called when the agents are first listed by the auction simulator
    #passes a list of the names of the agents (in order of ID)
    #agents will always be referred to by ID after this, so we
    #can use this list for reference if we need names.
    #note that this only passes strings, as we should never need to access actual agent objects from the UI
    def on_agents_discovered(self, agents):
        self.agents = agents
        
    #signifies the beginning of a round
    def on_round_started():
        pass
        
    #called when a card is auctioned off
    def on_auction_started(self, card):
        print("\nBidding on: ", card)
    
    #called when a bid is recieved from an agent
    def on_bid_received(self, card, agent_id, bid):
        print(self.agents[agent_id], "bid", bid)
    
    #called when a card is done being auctioned off
    def on_auction_finished(self, card, winner_id, price):
        print(self.agents[winner_id], " won", card.getName(), "at a price of", price)
    
    #called when a round has finished
    #scores is a list of the final score of each agent (in order of ID)
    #domiations is a list of tuples ids, where each tuple means the first agent dominated the second agent:
    #       that is [(1, 0), (2,1)] means agent 1 dominated agent 0, and agent 2 dominated agent 1
    #catagories is a list of the 5 individual catagory winners (again these are agent ids)
    #       in the order listed in auction_simulator.CATAGORIES
    def on_round_finished(self,scores, dominations, catagories):
        print("\nCalculating Scores:")
        for d in dominations:
            print("Agent", d[0], "dominated agent", d[1])
        for i in range(len(catagories)):
            print("Agent", catagories[i], "was best in", auction_simulator.CATAGORIES[i])
            
        print("\nFinal Scores:")
        print(scores)
        print(self.agents)
            
        
    #called when someone submits an illegal bid. Currently does nothing, but might be useful
    #the reason parameter can currently be "type" which means the bid wasn't an int,
    #   or  "budget" which means they bid more than their remaining budget.
    #illegal bids are automatically set to 0 (so on_bid_received will be called immediatly after this
    #   with a value of 0)
    def on_illegal_bid_received(self, agent_id, reason):
        print(self.agents[agent_id], "made an illegal bid:", reason)
        




