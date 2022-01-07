#card game
#shuffles 30 cards and creates a random deck

import random

player1Val=0
player1Score=0
player2Val=0
player2Score=0
shuffle=[]

#places the 30 cards in an array
deck=["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10",\
      "y1","y2","y3","y4","y5","y6","y7","y8","y9","y10",\
      "b1","b2","b3","b4","b5","b6","b7","b8","b9","b10"]

#shuffles the cards by taking them one at a time
#and places them into a new, shuffled deck
for x in range(0,30):
    card=random.choice(deck)
    deck.remove(card)
    shuffle.append(card)

#gives each player the top card on the deck
#removes the card taken from the deck
for x in range(0,29):
    player1 = shuffle[0]
    player2 = shuffle[1]
    shuffle.remove(player1)
    shuffle.remove(player2)
    print("Player 1, your card is",player1)
    print("Player 2, your card is",player2)

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
    elif player1 == "r7" or player1 == "y6" or player1== "b6":
        player1Val=7
    elif player1 == "r8" or player1 == "y8" or player1== "b8":
        player1Val=8
    elif player1 == "r9" or player1 == "y9" or player1 == "b9":
        player1Val=9
    elif player1 == "r10" or player1 == "y10" or player1 == "b10":
        player1Val=10

    print("Player 1 value is", player1Val)

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
    elif player2 == "r7" or player2 == "y6" or player2 == "b6":
        player2Val=7
    elif player2 == "r8" or player2 == "y8" or player2 == "b8":
        player2Val=8
    elif player2 == "r9" or player2 == "y9" or player2 == "b9":
        player2Val=9
    elif player2 == "r10" or player2 == "y10" or player2 == "b10":
        player2Val=10

    print("Player 2 value is", player2Val)


    if player1Val == player2Val:
        print("It's a draw!")
        player1Score=player1Score+player1Val
        player2Score=player2Score+player2Val
    elif player1Val > player2Val:
        print("Player 1 wins")
        player1Score=player1Score+player1Val
    else:
        print("Player 2 wins")
        player2Score=player2Score+player2Val
    print(x)
    print("game over")

print("player 1 got",player1Score)
print("player 2 got",player2Score)
