'''Q1 — The Stubborn Leaderboard
You are given a list of student records. Each record is a list with three values :
[name, score, age]
Sort the list by these rules in this exact priority order:
Score — descending (highest score comes first)
If two students have the same score → sort by age ascending (younger student comes first)
If score AND age are both the same → sort alphabetically by name ascending (A before Z)
Expected Output :
['Arjun', 92, 16]
['Kabir', 92, 16]
['Meera', 88, 16]
['Riya',  88, 17]
['Meera', 88, 17]
['Zara',  75, 17]'''

students = [
    ["Riya",  88, 17],
    ["Arjun", 92, 16],
    ["Meera", 88, 16],
    ["Kabir", 92, 16],
    ["Zara",  75, 17],
    ["Meera", 88, 17],
]

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][1] < students[j][1]:
            students[i], students[j] = students[j], students[i]

        elif students[i][1] == students[j][1]:

            if students[i][2] > students[j][2]:
                students[i], students[j] = students[j], students[i]

            elif students[i][2] == students[j][2]:

                if students[i][0] > students[j][0]:
                    students[i], students[j] = students[j], students[i]

for k in students:
    print(k)