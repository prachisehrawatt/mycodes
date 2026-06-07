lst=[12,24,36]
lst1=lst
lst2=lst+lst1

print(id(lst))
print(id(lst1))
print(id(lst2))

print(lst2)
lst2+=["1,2"]
print(id(lst))
print(id(lst1))
print(id(lst2))
print(lst2)

lst.pop()
print(lst)

del lst[0]
print(lst)

lst.remove(24)
print(lst)

lst1.clear()
print(lst1)