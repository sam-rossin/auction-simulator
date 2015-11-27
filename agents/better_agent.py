import bidding_agent

class BetterAgent(bidding_agent.BiddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.budget = budget
        self.ID = ID
        self.total = 0
        
        for card in cards:
            self.total += sum(card.getList()[1:4])
        
        
    def seeResults(self, card, winner, price, bids):
        self.total -= sum(card.getList()[1:4])
        if winner == self.ID:
            self.budget -= price
            
            
    def getBid(self, card, index):
        cardVal = sum(card.getList()[1:4])
        return (self.budget*cardVal)//self.total

