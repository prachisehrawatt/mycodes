import itertools
a = [1, 2]
b = [3, 4]
obj = itertools.product(a,b,repeat=2)
print(list(obj))