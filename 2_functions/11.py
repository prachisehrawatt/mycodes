pas = input('enter the password :')
lst = []
for i in pas:
    a = ord(i) + 6
    lst.append(chr(a))

print(lst)