import random
from itertools import accumulate

def roll_dice():
    return random.randint(1, 6)
n = int(input("Enter number of players: "))
user = []

for i in range(n):
    user.append(input(f"Enter Player {i} Name: "))

user.append('system')
scores = [[] for i in range(len(user))]

while True:

    for i in range(len(user)):
        print(f"{user[i]}'s Turn")
        roll = roll_dice()
        print("Rolled:", roll)

        scores[i].append(roll)

        if roll == 6: #repeat function
            print("Bonus Chance!")
            roll = roll_dice()
            print("Rolled Again:", roll)
            scores[i].append(roll)

        total = list(accumulate(scores[i]))[-1] #last score

        print("Total Score:", total)

        if total >= 50:
            print(f"{user[i]} Wins the Game!")
            exit() #break (why not) 

    print("=====Scoreboard=====")
    for i in range(len(user)):
        total = list(accumulate(scores[i]))[-1]
        print(user[i], ":", total)