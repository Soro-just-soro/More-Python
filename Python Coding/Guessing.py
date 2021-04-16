import random
number=random.randint(1,6)
chances=0
print("guess a number between 1 and 6")
while chances<3:
    guess=int(input("guess a number"))
    if guess==number:
        print("Congrats You Have Guessed Correctly!")
        break
    elif guess<number:
        print("Guess a Bigger Number")
    else:
        print("Guess a Lower Number")
    chances=chances+1
if not chances<3:
    print("You lose the Number was",number)