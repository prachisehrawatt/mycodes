nums = [0,0,1,1,1,2,2,3,3,4]
lst = [ ]
for i in nums:
    if i not in lst:
        lst.append(i)
print(lst)
