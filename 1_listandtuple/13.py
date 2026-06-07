''' Multi-Criteria Leaderboard

Topics Covered: Sorting with Custom Keys (Sec 12), Reversing (Sec 12), Nested Lists (Sec 10).
Scenario: You are building an arcade game leaderboard. The data is stored as a list of lists: [Player Name, Score].

Task:

Sort the leaderboard strictly using the .sort() method and a lambda key so that players are ranked by their Score in descending order (highest score first).
Tie-breaker rule: If two players have the exact same score, they must be sorted alphabetically by their Name (A to Z).
After the leaderboard is perfectly sorted, the arcade machine is unplugged! Use a built-in method to flip (reverse) the entire list in-place to simulate the display rendering upside down.'''



lst = []
n = int(input("enter number of players: "))

for i in range(n):
    name = input("enter player name : ")
    score = int(input("enter score : "))
    lst.append([name, score])


for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i][1] < lst[j][1]:
            lst[i], lst[j] = lst[j], lst[i]
        elif lst[i][1] == lst[j][1]:
            if lst[i][0] > lst[j][0]:
                lst[i], lst[j] = lst[j], lst[i]

print("Sorted Leaderboard:")

for i in lst:
    print(i)
lst.reverse()

print("Upside Down Leaderboard:")

for i in lst:
    print(i)