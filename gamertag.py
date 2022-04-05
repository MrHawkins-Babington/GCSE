#write a program to input a valid gamertag
#it cannot be longer than 15 characters

valid_gamertag = True

while valid_gamertag == True:
    print('''Your gamertag cannot be longer than 15 characters.
Please enter a new gamertag''')
    gamertag = input()
    gamertag_length = len(gamertag)
    if gamertag_length > 15:
        print("Your gamertag is too long")
    else:
        print(" gamertag accepted.")
        valid_gamertag = False
    
