import bidding_agent

class CopycatAgent(bidding_agent.BiddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.budget = budget
        self.ID = ID
        self.total = 0
        self.last_price = 0
        
        for card in cards:
            self.total += sum(card.list[1:])
        
        
    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price
        self.last_price = price
            
            
    def getBid(self, card, index):
        if self.last_price <= self.budget:
            return self.last_price
        return self.budget

