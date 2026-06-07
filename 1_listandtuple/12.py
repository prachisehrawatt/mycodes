''' Question 2: Matrix Column Extraction & Mutation

Topics Covered: Nested Lists (Sec 10), List Comprehensions (Sec 9), Modifying Lists (Sec 6), Sorting (Sec 12). Scenario: You have a 3x3 matrix representing scores in 3 different subjects across 3 different classes.

Task:

Using a list comprehension, extract the 2nd column (index 1) of the matrix into a brand new 1D list.
Sort this extracted 1D list in ascending order.
Replace the entire 1st row (index 0) of the original matrix with this newly sorted list.
Print the extracted column and the fully modified matrix.  '''



matrix = [
    [1, 2, 3],
    [2, 4, 8],
    [3, 6, 9]
]

column = []
for i in matrix:
    column.append(i[1])
column.sort()
matrix[0] = column

print("extracted column:", column)
print("modified matrix:")

for i in matrix:
    print(i)