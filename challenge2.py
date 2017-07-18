
"""
##Expected value of a game at a point
Given that you have X cards in hand, of which Y are black:
- The current expected value of the game
- Whether or not you would continue drawing cards
"""

X = -1 #Number of cards in hand
Black = -1 #Number of black cards in hand
currentCash = 0
while not int(X) in range(0,53):
    X = input("Please enter number of cards in hand (in range 1 - 52) : ")

while not int(Black) in range(0,27):
    Black = input("Please enter number of black cards in hand (in range 1 - 26) : ")
    

Red = X-Black #Calculate the number of Red cards in hand 
RedCost = -1 #You lose a dollar for picking a Red card
BlackCost = +1 #You win a dollar for picking a Black card

#Calculate number of cards remaining
RemainingRed = 26 - Red
RemainingBlack = 26 - Black
RemainingTotal = RemainingRed + RemainingBlack

#Check if end of game and if not calculate the expected value of the game
if RemainingTotal !=0:  
    EV = RemainingBlack/float(RemainingTotal)*BlackCost+RemainingRed/float(RemainingTotal)*RedCost
else:
    EV = 0
print 'The Current expected value of the game: ',EV

# Optimal stopping rule
if RemainingTotal !=0:              
    if EV < 0:print 'Quit the game'
    else:print 'Continue the game'
else:
    print 'End of game'


