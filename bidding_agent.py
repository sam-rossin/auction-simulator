#bidding agent class

class BiddingAgent:
    #5 second time limit.
    #This function is given the list of all cards to be auctioned,
    #an integer ID number, the total number of players, and an integer
    #starting budget.  Each card is in the format given above, and
    #appears in the order it will be auctioned off.
    #The ID number is your agents index, which will be important for
    #interpreting the results of each auction.  And the budget is how
    #much you start with.  Agents need to keep track of their own budget.
    def __init__(self, cards, ID, players, budget):
        pass
    
    #.1 second time limit.
    #This function is used by the system to inform your agent on the
    #results of each auction.  In particular, it indicates that agent
    #<winner> won card <card> and will pay <price>.  The list <bids>
    #contains all bids made by all agents, ordered by agent IDs.  You'll
    #want to update your budget here in the event that you were the winner,
    #but you may also wish to record other information, such as the sale
    #price of the card, the bids of other agents, or the current category
    #scores of other agents.
    def seeResults(self, card, winner, price, bids):
        pass
    
    #.1 second time limit
    #This function is passed a card and an integer indicating the index of
    #that card in the auction.  It should return an integer bid b at least 0,
    #and at most your remaining budget.  Your agent is responsible for keeping
    #track of your remaining budget.  Invalid bids will be automatically set
    #to 0.
    def getBid(self, card, index):
        pass
    
    
    #allow bidding agents to be printed easily
    def __repr__(self):
        return self.__class__.__name__
    
    
    

