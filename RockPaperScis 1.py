#rock paper scissors

#Rock smashes scissors.
#Paper covers rock.
#Scissors cut paper.

#We need to be able to make random choices
import random


#stage 1 - set up the basic game choices
#user makes their choice
playerChoice = input("Enter a choice(rock, paper or scissors)")

choices = ["rock","paper","scissors"]
computerChoice = random.choice(choices)

print(playerChoice)
print(computerChoice)
