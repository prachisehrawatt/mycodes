from collections import defaultdict
x = defaultdict(list)
x[1].append("name")
x[1].append("marks")
print(x.items())
print(x.keys())
print(x.values())
print(x)