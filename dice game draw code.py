#code removed from full project to allow testing
#trying to code what to do if game ends in a draw

import random
player1total = int(input("enter a number"))
player2total = int(input("enter a number"))

if player1total == player2total:
    draw = 1
    print("It's a draw!")
    print("Each player will throw a dice. Highest score wins.")
    while draw == 1:
        play1 = input("\nPlayer 1, press enter to roll the dice!")
        throw1 = random.randint(1,6)
        print("\nPlayer 1,you threw a",throw1)
        
        play2 = input("\nPlayer 2, press enter to roll the dice!")
        throw2 = random.randint(1,6)
        print("\nPlayer 2,you threw a",throw2)
        if throw1 == throw2:
            print("\Oh no! It's another draw!")
            draw = 1
        elif throw1 > throw2:
            print("\nCongratulations, player 1, you are the winner!")
            draw = 2
        else:
            print("\nCongratulations, player 2, you are the winner!")
            draw = 2
elif player1total > player2total:
    print("\nCongratulations, player 1, you are the winner!")
else:
    print("\nCongratulations, player 2, you are the winner!")
