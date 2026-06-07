'''2D List Matrix Operations : Write a Python program that works with a 2D list representing a class timetable or marks table.
The program should :-

1. Display the 2D list in matrix form
2. Find the sum of each row
3. Find the sum of each column
4. Replace all values less than 50 with "F"
5. Create a copy of the original matrix before modifying it
6. Reverse the order of rows and print the updated matrix'''


row = 3
lst = []

'''for i in range(3):
    row_val = input("enter the values ( with spaces ) :")
    temp_lst = []
    for j in row_val.split() :
        temp_lst.append(int(j))
    lst.append(temp_lst)'''

lst = [
[78, 45, 90, 67],
[34, 88, 55, 40],
[92, 71, 48, 60]
]

#SUM
for k in lst :
    print(sum(k))

#col_sum
print(lst[0][0]+lst[1][0]+lst[2][0])
print(lst[0][1]+lst[1][1]+lst[2][1])
print(lst[0][2]+lst[1][2]+lst[2][2])


#COPY
modified_lst = lst.copy()
for i in modified_lst:
    for index,j in enumerate(i):
        if j<=50:
            i[index]='F'

print(modified_lst[::-1])

