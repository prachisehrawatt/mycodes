#view 1 - Top Scorers

def show_top_scorers(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):

            runs_i, balls_i = temp[i][1], temp[i][2]
            runs_j, balls_j = temp[j][1], temp[j][2]

            if runs_j > runs_i:
                temp[i], temp[j] = temp[j], temp[i]

            elif runs_j == runs_i and balls_j < balls_i:
                temp[i], temp[j] = temp[j], temp[i]

    print("______ Top Scorers ______")

    for i in range(len(temp)):
        print(f"{i+1}. {temp[i][0]} | Runs: {temp[i][1]} | Balls: {temp[i][2]}")


#view 2 - Strike Rate Kings

def show_strike_rate(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):

            try:
                sr1 = (temp[i][1] / temp[i][2]) * 100
            except ZeroDivisionError:
                sr1 = 0

            try:
                sr2 = (temp[j][1] / temp[j][2]) * 100
            except ZeroDivisionError:
                sr2 = 0

            if sr2 > sr1:
                temp[i], temp[j] = temp[j], temp[i]

    print("______ Strike Rate Kings ______")

    for i in range(len(temp)):

        try:
            sr = (temp[i][1] / temp[i][2]) * 100
        except ZeroDivisionError:
            sr = 0

        print(f"{i+1}. {temp[i][0]} | SR: {round(sr, 2)} | Runs: {temp[i][1]}")


#view 3 - Boundary Hitters

def show_boundary_hitters(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):

            total_i = temp[i][3] + temp[i][4]
            total_j = temp[j][3] + temp[j][4]

            if total_j > total_i:
                temp[i], temp[j] = temp[j], temp[i]

            elif total_j == total_i and temp[j][4] > temp[i][4]:
                temp[i], temp[j] = temp[j], temp[i]

    print("______ Boundary Hitters ______")

    for i in range(len(temp)):

        total = temp[i][3] + temp[i][4]

        print(
            f"{i+1}. {temp[i][0]} | Boundaries: {total} "
            f"({temp[i][3]} fours, {temp[i][4]} sixes)"
        )


#view 4 - Alphabetical Order

def show_alphabetical(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):

            if temp[j][0] < temp[i][0]:
                temp[i], temp[j] = temp[j], temp[i]

    print("______ Alphabetical ______")

    for i in range(len(temp)):
        print(f"{i+1}. {temp[i][0]}")


# Main Program

data = [
    ["Rohit",   72, 45, 6, 3],
    ["Virat",   55, 42, 4, 2],
    ["Rahul",   30, 28, 2, 1],
    ["Hardik",  48, 22, 3, 4],
    ["Jadeja",  20, 18, 1, 1],
    ["Dhoni",   36, 15, 2, 3],
    ["Shami",    8, 10, 0, 0],
    ["Bumrah",   0,  0, 0, 0],
]

while True:

    print("===== Cricket Scorecard Sorter =====")
    print("1. Top Scorers")
    print("2. Strike Rate Kings")
    print("3. Boundary Hitters")
    print("4. Alphabetical Order")
    print("5. Original Scorecard")
    print("6. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue

    if ch == 1:
        show_top_scorers(data)

    elif ch == 2:
        show_strike_rate(data)

    elif ch == 3:
        show_boundary_hitters(data)

    elif ch == 4:
        show_alphabetical(data)

    elif ch == 5:
        print("______ Original Scorecard ______")
        for player in data:
            print(player)

    elif ch == 6:
        print("THANK YOU!")
        break

    else:
        print("Please choose a valid option (1-6).")






        