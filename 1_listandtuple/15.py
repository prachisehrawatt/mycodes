'''lst=['a','A','r','f','k','Q']
vowels=[i for i in lst if i in 'AEIOU' ]
print(vowels)

scores = [45, 88, 92, 33, 50, 71, 12]

lst = [i for i in scores if i>50]
print(lst)

matrix = [
    [5, 12, 8],
    [20, 3, 15],
    [9, 11, 4]
]

lst = [j for i in matrix for j in i if j>10]
lst1 = [i[0] for i in matrix ]
print(lst1)
print (lst)'''

matrix = []
lst=[[0]*3 for i in range(3)]
print(matrix)
print(lst)
