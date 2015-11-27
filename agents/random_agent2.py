import bidding_agent
import random

class RandomAgent(bidding_agent.BiddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.budget = budget
        self.ID = ID
        
    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price
            
    def getBid(self, card, index):
        return random.randint(0, self.budget)
        