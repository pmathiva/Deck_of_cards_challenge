

"""
#Expected value of standard deck of 52 cards
The output is a matrix with X- axis as the number of Red cards in hand and
 Y-axis as the number of Black cards in hand
 Ex: Matrix element corresponding to X=1 and Y=5 gives the Expected value of the game 
 when 1 red card and 5 black cards  are in hand
 """
import pandas
import seaborn as sns
import numpy as np
import matplotlib as plt 

def ExpectedValue():
    red = 52
    black = 52
    table = []

    for i in reversed(range(red+1)):
        col = []
        for j in reversed(range(black+1)):
            rem = i+j
            if rem:
                blackEV = j/float(rem)*1.0 if  j!=0 else 0
                redEV = i/float(rem)*-1.0 if i!=0 else 0
                EV = blackEV+redEV
                col.append(EV)
            else:col.append(0)
        table.append(col)
    df = pandas.DataFrame(table).transpose()
    
    print df
    
ExpectedValue() # Prints the matrix of expected value of the deck of cards
