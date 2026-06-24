from itertools import permutations

x = [1,2,3]

obj = permutations(x)
print(list(obj))

obj = permutations(x,2)
print(list(obj))