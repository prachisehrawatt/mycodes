'''Q3. Write a program to "flatten" the 2D list into a 1D list.

map_grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# Expected Output: [1, 1, 1, 1, 0, 1, 1, 1, 1]'''

map_grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

flattened_lst = [j for i in map_grid for j in i]

print(f"Flattened List: {flattened_lst}")


