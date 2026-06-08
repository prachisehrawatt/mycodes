scorecard = [
    ["Rohit",   72, 45, 6, 3],
    ["Virat",   55, 42, 4, 2],
    ["Rahul",   30, 28, 2, 1],
    ["Hardik",  48, 22, 3, 4],
    ["Jadeja",  20, 18, 1, 1],
    ["Dhoni",   36, 15, 2, 3],
    ["Shami",    8, 10, 0, 0],
    ["Bumrah",   4,  6, 0, 0],
]
print("1. Top Scorers")
#view 1 - Top Scorers

#def show_top_scorers(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i, len(temp)):
            if temp[j][1] > temp[i][1]:
                temp[i], temp[j] = temp[j], temp[i]
            elif temp[j][1] == temp[i][1]:
                if temp[j][2] < temp[i][2]:
                    temp[i], temp[j] = temp[j], temp[i]

    print("_______Top Scorers______-")

    for i in range(len(temp)):
        print(i + 1, temp[i][0], "| Runs:", temp[i][1], "| Balls:", temp[i][2])

#view 2 - Strike Rate Kings

#def show_strike_rate(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            sr1 = (temp[i][1] / temp[i][2]) * 100
            sr2 = (temp[j][1] / temp[j][2]) * 100
            if sr2 > sr1:
                temp[i], temp[j] = temp[j], temp[i]

    print("______Strike Rate Kings______")

    for i in range(len(temp)):
        sr = (temp[i][1] / temp[i][2]) * 100
        print(i + 1, ".", temp[i][0], "| SR:", round(sr, 2), "| Runs:", temp[i][1])


#view 3 - Boundary Hitters

#def show_boundary_hitters(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            total1 = temp[i][3] + temp[i][4]
            total2 = temp[j][3] + temp[j][4]
            if total2 > total1:
                temp[i], temp[j] = temp[j], temp[i]
            elif total2 == total1:
                if temp[j][4] > temp[i][4]:
                    temp[i], temp[j] = temp[j], temp[i]

    print("______Boundary Hitters______")

    for i in range(len(temp)):
        total = temp[i][3] + temp[i][4]

        print(i + 1, temp[i][0], "| Boundaries:", total, "(", temp[i][3], "fours,", temp[i][4], "sixes )" )

#view 4 - Alphabetical

#def show_alphabetical(data):

    temp = data.copy()

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[j][0] < temp[i][0]:
                temp[i], temp[j] = temp[j], temp[i]

    print("_____Alphabetical_____")

    for i in range(len(temp)):
        print(i + 1, temp[i][0])

#main program
while True:
    

show_top_scorers(scorecard)

show_strike_rate(scorecard)

show_boundary_hitters(scorecard)

show_alphabetical(scorecard)

print("______Original Scorecard______")

for player in scorecard:
    print(player)
