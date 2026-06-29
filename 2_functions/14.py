'''lst = [1,2,57,8]
x = list(filter(lambda x: x%2==0 , lst))
print(x)
lst1 = [ 'cat','lion','rabbit','bat']
y = list(filter(lambda x: len(x)>3 , lst1))
print(y)
z = sorted(list(filter(lambda x: sorted(x),lst1)))
print(z)
'''

inventory = [
    ("Laptop", 5),
    ("Mouse", 0),
    ("Keyboard", 3),
    ("Monitor", 0)
]
x = list(filter(lambda x: x[1]==0 , inventory))
print(x)
from functools import reduce
lst = [1,2,57,8]
obj = reduce(lambda x,y : x if x>y else y  , lst)
print(obj)


students = [
    ('Alice', 3.8),
    ('Bob', 3.5),
    ('Charlie', 3.9),
    ('David', 3.2)
]
obj1 = sorted(students , key = lambda x : len(x[0]) , reverse = True)
print(obj1)

employees = [
    ("Anna", 30, 50000),
    ("Dave", 25, 90000),
    ("John", 45, 75000)
]

obj2 = sorted(employees , key = lambda x : x[2])
print(obj2)