
# COMPUTER QUIZ GAME ( Mini Project - Week 2)

print("       Welcome to the Computer Quiz Game!      ")
playing = input("do you want to play? (yes/no): ").lower()

if playing != "yes":
    print("Okay, Maybe next time!")
else:
    print("Great! Let's play")

score = 0

# Question 1
answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


# Question 3
answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What does ROM stand for? ").lower()

if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

total_ques = 4
perc = (score / total_ques) * 100

print("     Quiz Finished      ")
print("Your", score, "questions are correct!")
print("You scored", perc , "%")