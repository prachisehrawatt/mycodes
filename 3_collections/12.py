from itertools import groupby

'''x = ['cat','cat','dog','snake','rabbit','cat']
for key , group in groupby(x):
    print(key,list(group))'''

students = sorted([
    ('Alice', 'A'),
    ('Charlie', 'B'),
    ('Bob', 'A'),
    ('David', 'C'),
    ('Eve', 'B')
], key=lambda x: len(x[0]))

print(students)