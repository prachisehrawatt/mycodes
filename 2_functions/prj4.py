# MYSTERY ISLAND ADVENTURE :  Mini Project ( Week - 2 )

name = input("Enter your name: ")
print("Welcome,", name)

ch = input("You are at a crossroads. Go left or right? ").lower()

if ch == "left":
    ch1 = input("You see a river. Swim or walk? ").lower()

    if ch1 == "swim":
        print("A crocodile got you. You lost!")

    else:
        print("You found a treasure. You win!")

elif ch == "right":
    print("You fell into a hole. You lost!")

else:
    print("Invalid choice. Game over.")