#card game
#shuffles 30 cards and creates a random deck

import random

player1Val=0        #variable used to assign a numerical value for each drawn card
player2Val=0
player1Score=0      #running score during game for player 1 and player 2 
player2Score=0
shuffle=[]          #empty deck for the shuffled cards to be put in at the start of the game
player1deck=[]      #empty decks for the winning hands from each turn to be put in      
player2deck=[]       

#the 30 cards that are in the deck placed into an array
deck=["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10",\
      "y1","y2","y3","y4","y5","y6","y7","y8","y9","y10",\
      "b1","b2","b3","b4","b5","b6","b7","b8","b9","b10"]

#shuffles the cards by taking them one at a time
#places them into a new, shuffled deck
for x in range(0,30):
    card=random.choice(deck)
    deck.remove(card)
    shuffle.append(card)

cont=input("The deck has been shuffled. Are you ready to play? Press any key to continue")


#gives each player the top card on the deck
#removes the card taken from the deck
for x in range(0,15):
    player1 = shuffle[0]        #player 1 gets the top card of the deck, player 2 the second
    player2 = shuffle[1]
    shuffle.remove(player1)     #the drawn cards are removed from the shuffled deck so they can only be taken once
    shuffle.remove(player2)
    print()
    print("This is go ",x+1)
    print("Player 1, your card is",player1)
    print("Player 2, your card is",player2)
    cont=input("press any key to continue")

    #checks to see if the cards are the same colour
    #If cards are the same colour highest value wins
    #if cards are different colours win based on rock paper scissors type scenario
    #red beats black
    #yellow beats red
    #black beats yellow

    #assigns the card taken a colour value
    if player1== "r1" or player1== "r2" or player1== "r3" or player1== "r4" or player1== "r5"\
       or player1== "r6" or player1== "r7" or player1== "r8" or player1== "r9" or player1== "r10":
        player1colour = "red"
    elif player1== "y1" or player1== "y2" or player1== "y3" or player1== "y4" or player1== "y5"\
       or player1== "y6" or player1== "y7" or player1== "y8" or player1== "y9" or player1== "y10":
        player1colour = "yellow"
    elif player1== "b1" or player1== "b2" or player1== "b3" or player1== "b4" or player1== "b5"\
       or player1== "b6" or player1== "b7" or player1== "b8" or player1== "b9" or player1== "b10":
        player1colour = "black"

    if player2== "r1" or player2== "r2" or player2== "r3" or player2== "r4" or player2== "r5"\
       or player2== "r6" or player2== "r7" or player2== "r8" or player2== "r9" or player2== "r10":
        player2colour = "red"
    elif player2== "y1" or player2== "y2" or player2== "y3" or player2== "y4" or player2== "y5"\
       or player2== "y6" or player2== "y7" or player2== "y8" or player2== "y9" or player2== "y10":
        player2colour = "yellow"
    elif player2== "b1" or player2== "b2" or player2== "b3" or player2== "b4" or player2== "b5"\
       or player2== "b6" or player2== "b7" or player2== "b8" or player2== "b9" or player2== "b10":
        player2colour = "black"

##    print("Player 1, your card colour is ",player1colour)
##    print("Player 2, your card colour is ",player2colour)
##    cont=input("press any key to continue")

    #assigns the card taken a numerical value
    if player1 == "r1" or player1 == "y1" or player1 == "b1":
        player1Val=1
    elif player1 == "r2" or player1 == "y2" or player1 == "b2":
        player1Val=2
    elif player1 == "r3" or player1 == "y3" or player1 == "b3":
        player1Val=3
    elif player1 == "r4" or player1 == "y4" or player1 == "b4":
        player1Val=4
    elif player1 == "r5" or player1 == "y5" or player1 == "b5":
        player1Val=5
    elif player1 == "r6" or player1 == "y6" or player1 == "b6":
        player1Val=6
    elif player1 == "r7" or player1 == "y7" or player1== "b7":
        player1Val=7
    elif player1 == "r8" or player1 == "y8" or player1== "b8":
        player1Val=8
    elif player1 == "r9" or player1 == "y9" or player1 == "b9":
        player1Val=9
    elif player1 == "r10" or player1 == "y10" or player1 == "b10":
        player1Val=10


    if player2 == "r1" or player2 == "y1" or player2 == "b1":
        player2Val=1
    elif player2 == "r2" or player2 == "y2" or player2 == "b2":
        player2Val=2
    elif player2 == "r3" or player2 == "y3" or player2 == "b3":
        player2Val=3
    elif player2 == "r4" or player2 == "y4" or player2 == "b4":
        player2Val=4
    elif player2 == "r5" or player2 == "y5" or player2 == "b5":
        player2Val=5
    elif player2 == "r6" or player2 == "y6" or player2 == "b6":
        player2Val=6
    elif player2 == "r7" or player2 == "y7" or player2 == "b7":
        player2Val=7
    elif player2 == "r8" or player2 == "y8" or player2 == "b8":
        player2Val=8
    elif player2 == "r9" or player2 == "y9" or player2 == "b9":
        player2Val=9
    elif player2 == "r10" or player2 == "y10" or player2 == "b10":
        player2Val=10

##    print("Player 1 value is", player1Val)
##    print("Player 2 value is", player2Val)
##    cont=input("press any key to continue")

    #checks to see if card colours are the same

    if player1colour == player2colour:
        if player1Val > player2Val:
            print("Player 1 wins")
            player1Score=player1Score+player1Val
            print("Player 1's score is ",player1Score)
            player1deck.append(player1)     #the winning cards are put into player 1's pile
            player1deck.append(player2)
        elif player2Val > player1Val:
            print("Player 2 wins")
            player2Score=player2Score+player2Val
            print("Player 2's score is ",player2Score)
            player2deck.append(player1)     #the winning cards are put into player 2's pile
            player2deck.append(player2)

#    cont=input("press any key to continue")
    

    #checks to see if card colour are different

    if player1colour != player2colour:
        print("The cards you have drawn are different colours so...")
        if player1colour == "red" and player2colour == "black":
            print("Red beats black!")
            player1Score = player1Score + player1Val
            player1deck.append(player1)
            player1deck.append(player2)
        elif player1colour == "yellow" and player2colour == "red":
            print("Yellow beats Red!")
            player1Score = player1Score + player1Val
            player1deck.append(player1)
            player1deck.append(player2)
        elif player1colour == "black" and player2colour == "yellow":
            print("Black beats Yellow!")
            player1Score = player1Score + player1Val
            player1deck.append(player1)
            player1deck.append(player2)
            
        elif player2colour == "red" and player1colour == "black":
            print("Red beats black!")
            player2Score = player2Score + player2Val
            player2deck.append(player1)
            player2deck.append(player2)
        elif player2colour == "yellow" and player1colour == "red":
            print("Yellow beats Red!")
            player2Score = player2Score + player2Val
            player2deck.append(player1)
            player2deck.append(player2)
        elif player2colour == "black" and player1colour == "yellow":
            print("Black beats Yellow!")
            player2Score = player2Score + player2Val
            player2deck.append(player1)
            player2deck.append(player2)

    print("Player 1's score is ",player1Score)
    print("Player 2's score is ",player2Score)
    cont=input("press any key to continue")

#winner announced at the end of the game
if player1Score == player2Score:
    print("Wow, a draw! Well done both players.")
    print("Player 1's winning hands - ",player1deck)
    print("Player 2's winning hands - ",player2deck)
elif player1Score > player2Score:
    print("Player 1 got ",player1Score, "and player 2 got ",player2Score)
    print("Player 1 wins!")
    print("Player 1's winning hands - ",player1deck)
else:
    print("Player 2 got ",player2Score, "and player 1 got ",player1Score)
    print("Player 2 wins!")
    print("Player 2's winning hands - ",player2deck)
