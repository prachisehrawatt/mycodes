from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
p2 = Point(x=5, y=15)

# Access fields
print(p1.items())  # Output: 10 20
print(p1[0], p1[1]) 