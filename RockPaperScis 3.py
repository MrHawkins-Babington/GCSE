#rock paper scissors

#Rock smashes scissors.
#Paper covers rock.
#Scissors cut paper.

#We need to be able to make random choices
import random


#stage 3 Set up the while loop
while True:

    playerChoice = input("Enter a choice(rock, paper or scissors)")

    choices = ["rock","paper","scissors"]
    computerChoice = random.choice(choices)

    print(f"\nYou chose {playerChoice}, computer chose {computerChoice}.\n")


    if playerChoice == computerChoice:
        print(f"Both players selected {playerChoice}. It's a tie!")
    elif playerChoice == "rock":
        if computerChoice == "Scissors":
            print("Rock smashes scissors! You Win!")
        else:
            print("Paper covers rock. You lose!")
    elif playerChoice == "paper":
        if computerChoice == "rock":
            print("paper covers rock! You win!")
        else:
            print("Scissors cuts paper. You lose!")
    elif playerChoice == "scissors":
        if computerChoice == "paper":
            print("scissors cut paper! You win!")
        else:
            print("rock smashes scissors. You lose!")

    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        break


