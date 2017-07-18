

"""
#Simulation of playing cards
Rules of the game
- You have a standard deck of 52 cards facing down
- You can only draw one card at a time
- For each black card you draw, you earn $1
- For each red card you draw, you lose $1
- You may choose to stop drawing cards at any time and walk away with your cumulative winnings
"""

import numpy
import collections
import random

redCost = 1
blackCost = -1

cards = ['R','B']
deck = numpy.repeat(cards,26).tolist() #Create a deck of 52 cards
game = []
currentCash = 0

print 'Initial Deck: ',collections.Counter(deck)

while deck: #Loop till there are cards remaining in the deck
    
    pick = random.choice(deck) #A random draw of a card
    game.append(pick)          
    deck.remove(pick)
    if pick == 'B':currentCash+=1 #If the card is black you get a dollar
    else:currentCash+=-1            #If teh card is red you lose a dollar
    blackEV = (deck.count('B')/float(len(deck))*blackCost) if  deck.count('B')!=0 else 0 #The Eepected value of the game based on remaining black cards
    redEV = (deck.count('R')/float(len(deck))*redCost) if deck.count('R')!=0 else 0 #The expected value of the game based on remaining red cards
    EV = blackEV + redEV #The total expected value of the game 
     
    if EV < currentCash:break  #The optimal stopping rule

print '\nNumber of draws: ',len(game)   #The total number of cards drawn at the end of the game
print '\nGame: ',game                   #The final sequence of cards drawn 
print '\nAmount Won: $',currentCash      #Amount won at the end of the game



