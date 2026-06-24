import random

print("====WELCOME TO THE GAME OF DICE====")

user_score = 0
system_score = 0

for i in range (1,4):
   message = f"Now , Round {i} starts !"
   user = random.randint(1,6)
   system = random.randint(1,6)
   print(f"THE NUMBER DRAWN BY USER IS {user} and THE NUMBER DRAWN BY SYSTEM IS {system}")
  
   if user > system:
        user_score += 1
        print("User wins this round!")

   elif system > user:
        system_score += 1
        print("System wins this round!")

   else:
        print("Round tied!")


print("===== FINAL SCORE =====")
print(f"User Score   : {user_score}")
print(f"System Score : {system_score}")

if user_score > system_score:
    print("USER WINS THE GAME!")

elif system_score > user_score:
    print("SYSTEM WINS THE GAME!")

else:
    print("GAME TIED!")



  