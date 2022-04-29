#dice game - throw a six sided die
#print the result

import random
score = 0

throw1 = random.randint(1,6)
throw2 = random.randint(1,6)
print(throw1,throw2)

if throw1 == throw2:
    print("You threw a double!")
    score = (throw1 + throw2) + 10
    extraThrow = random.randint(1,6)
    print("You threw an extra ",extraThrow)
    score = score + extraThrow 
else:
    print("That isn't a double...")
    score = (throw1 + throw2) - 5


print("Your score is ",score)


