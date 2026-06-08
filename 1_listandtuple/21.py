'''Q2. Find the sum of both diagonal numbers : 
grid = [
    [10, 2, 3],
    [4, 20, 6],
    [7, 8, 30]
]

# Expected Output: 60 (since 10 + 20 + 30 = 60)'''

grid = [
    [10, 2, 3],
    [4, 20, 6],
    [7, 8, 30]
]

sum = sum(grid[i][i] for i in range(len(grid)))
print("Sum of diagonal elements =", sum)