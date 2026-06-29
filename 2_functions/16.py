
def two_pointers(lst):
    i=0
    for j in range (1,len(lst)):
        if lst[j]!= lst[j-1]:
            i=i+1
            lst[i]=lst[j]
    return i+1


lst = [0, 1, 1, 2, 2, 3, 4, 4, 4, 5]
print(lst)
x=two_pointers(lst)
for values in range(x):
    print(lst[values], end=' ')
print('\n',lst)