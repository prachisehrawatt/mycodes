from itertools import combinations	
a = [1, 2, 3]
obj = combinations(a,2) 
print(list(obj))

from itertools import permutations
obj1 = permutations(a,2)
print(list(obj1))