#2 player card game - J277 coding project

#creating the deck and picking a card at random

#I want to be able to shuffle the deck of cards
#My initial idea is to create a 2D array with the cards in, pick one at random
# and put that into a new array that holds the shuffled deck.

import random

#set up the colours of the hands
red=1
yellow=2
black=3

#set up the values of each card
redHand=[1,2,3,4,5,6,7,8,9,10]
yellowHand=[1,2,3,4,5,6,7,8,9,10]
blackHand=[1,2,3,4,5,6,7,8,9,10]

#choose a random colour
ranColour=random.randint(1,3)
#choose a random value
ranValue=random.randint(1,10)

if ranColour == 1:
    hand="Red"
elif ranColour == 2:
    hand = "Yellow"
else:
    hand = "Black"

print(hand,ranValue)
