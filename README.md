### Auction Simulator

An imcomplete auction simulator, based on the rules specified in poster.pdf. It consists of
the following parts:

1. auction_simulator.py -- the main program that runs the auction. The only thing
    in here that desparatly needs to be changed is the "generate_cards" function. Currently
    the function is completely random, it should be modified to use different decks based on the
    round or something.
    
    Right now the program just runs all rounds straight through when it is run. It would need
    to be restructured if you want to actually control it from the UI, currenly the model is
    that the UI will just be for display purposes.
    
2. user_interface.py -- a class with functions that are called when there is information
    available that might be needed by the UI. These fuctions need to be changed to work with
    a graphical display, they currently just print the information.
    
3. bidding_agent.py -- the basic BiddingAgent class that agents are subclasses of.

4. card.py -- the card class. Contains the card information, as well as various getters.

5. agents folder -- this folder is where any agents should be placed. The auction simulator
    uses any class it finds in this folder that is a subclass of BiddingAgent. Note that the
    empty file \__init\__.py must be left in this folder for the auction simulator to work
    properly (because of how python modules work).
    
    This folder currently contains 5 test agents:
  * RandomAgent and RandomAgent2 which bid a random amount of their remaining budget.
  * CopycatAgent which bids whatever the last price paid was.
  * ProportionalAgent which bids based on how valuble the cards stats are as a proportion
        of the total stats form all the cards.
  * BetterAgent which is the same as proportional agent, except it only cares about the
        first 3 stats on each card.
