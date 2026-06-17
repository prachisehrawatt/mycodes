# ROCK PAPER SCISSORS ( Mini Project - Week 2 )

import random

lst = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:

    x = input("Rock/Paper/Scissors (or quit): ").lower()

    if x == "quit":
        break

    if x not in lst:
        continue

    y = random.choice(lst)
    print("Computer picked",y)

    if x == y:
        print("Tie!")

    elif (x == "rock" and y == "scissors") or (x == "paper" and y == "rock") or (x == "scissors" and y == "paper"):
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
