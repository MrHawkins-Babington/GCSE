#rock paper scissors

#Rock smashes scissors.
#Paper covers rock.
#Scissors cut paper.

#We need to be able to make random choices
import random

##stage 5 Set up the end game conditions
playerTotal = 0
computerTotal = 0
playGame = True

while playGame == True :

    playerChoice = input("Enter a choice(rock, paper or scissors)")

    choices = ["rock","paper","scissors"]
    computerChoice = random.choice(choices)

    print(f"\nYou chose {playerChoice}, computer chose {computerChoice}.\n")


    if playerChoice == computerChoice:
        print(f"Both players selected {playerChoice}. It's a tie!")

    elif playerChoice == "rock":
        if computerChoice == "Scissors":
            playerTotal = playerTotal + 1
            print("Rock smashes scissors! You Win!")
            print("Player score :",playerTotal, "computer score:",computerTotal)
            if playerTotal == 3 or computerTotal == 3:
                playGame == False
                break
                
        else:
            computerTotal = computerTotal + 1
            print("Paper covers rock. You lose!")
            print("Player score :",playerTotal, "computer score:",computerTotal)
            if playerTotal == 3 or computerTotal == 3:
                playGame == False
                break

    elif playerChoice == "paper":
        if computerChoice == "rock":
            playerTotal = playerTotal + 1
            print("paper covers rock! You win!")
            print("Player score :",playerTotal, "computer score:",computerTotal)
            if playerTotal == 3 or computerTotal == 3:
                playGame == False
                break
        else:
            computerTotal = computerTotal + 1
            print("Scissors cuts paper. You lose!")
            print("Player score :",playerTotal, "computer score:",computerTotal)
            if playerTotal == 3 or computerTotal == 3:
                playGame == False
                break

    elif playerChoice == "scissors":
        if computerChoice == "paper":
            playerTotal = playerTotal + 1
            print("scissors cut paper! You win!")
            print("Player score :",playerTotal, "computer score:",computerTotal)
            if playerTotal == 3 or computerTotal == 3:
                playGame == False
                break
        else:
            computerTotal = computerTotal + 1
            print("rock smashes scissors. You lose!")
            print("Player score :",playerTotal, "computer score:",computerTotal)
            if playerTotal == 3 or computerTotal == 3:
                playGame == False
                break



