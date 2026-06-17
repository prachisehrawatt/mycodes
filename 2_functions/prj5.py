# PASSWORD MANAGER : Mini Project ( Week - 2 )

m = "admin123"

p = input("Enter master password: ")

if p != m:
    print("Wrong password!")
    
else:
    mode = input("Add or View? ").lower()

    if mode == "add":
        a = input("Account: ")
        pw = input("Password: ")

        with open("passwords.txt", "a") as f:
            f.write(a + "|" + pw + "\n")

        print("Saved!")

    elif mode == "view":
        with open("passwords.txt", "r") as f:
            for l in f:
                a, pw = l.strip().split("|")
                print("User:", a, "| Password:", pw)