# NUMBER GUESSER ( Mini Project - Week 2 )

import random

x=int(input("ENTER THE MAX RANGE : "))

number = random.randint(1,x)
guesses = 0

while True:
    guess = int(input("Guess a number: "))
    guesses += 1

    if guess > number:
        print("higher!")
    elif guess < number:
        print("lower!")
    else:
        print("You got it in", guesses, "guesses!")
        
        break
