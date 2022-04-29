#dice game - throw a six sided die
#print the result

import random
Player1score = 0
player2score = 0

#player 1 go
throw1 = random.randint(1,6)
throw2 = random.randint(1,6)
print(throw1,throw2)

if throw1 == throw2:
    print("You threw a double!")
    player1score = (throw1 + throw2) + 10
    extraThrow = random.randint(1,6)
    print("You threw an extra ",extraThrow)
    player1score = player1score + extraThrow 
else:
    print("That isn't a double...")
    player1score = (throw1 + throw2) - 5

if player1score < 0:
    player1score = 0
else:
    player1score = player1score

#player 2 go
throw1 = random.randint(1,6)
throw2 = random.randint(1,6)
print(throw1,throw2)

if throw1 == throw2:
    print("You threw a double!")
    player2score = (throw1 + throw2) + 10
    extraThrow = random.randint(1,6)
    print("You threw an extra ",extraThrow)
    player2score = player2score + extraThrow 
else:
    print("That isn't a double...")
    player2score = (throw1 + throw2) - 5

if player2score < 0:
    player2score = 0
else:
    player2score = player2score


print("Player 1 - Your score is ",player1score)
print("Player 2 - Your score is ",player2score)


