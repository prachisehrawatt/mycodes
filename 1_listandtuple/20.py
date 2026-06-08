'''Q1 : 2 matrix A,B. Find its sum
matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]

# Expected Output: [[6, 8], [10, 12]] '''


matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]
sum =[[matrix_A[i][j] + matrix_B[i][j]
           for j in range(len(matrix_A[0]))]
           for i in range(len(matrix_A))]

print(sum)