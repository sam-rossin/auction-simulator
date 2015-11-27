import bidding_agent

class ProportionalAgent(bidding_agent.BiddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.budget = budget
        self.ID = ID
        self.total = 0
        
        for card in cards:
            self.total += sum(card.getList()[1:])
        
        
    def seeResults(self, card, winner, price, bids):
        self.total -= sum(card.getList()[1:])
        if winner == self.ID:
            self.budget -= price
            
            
    def getBid(self, card, index):
        cardVal = sum(card.list[1:])
        return (self.budget*cardVal)//self.total

