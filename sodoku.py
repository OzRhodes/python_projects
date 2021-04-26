# A simple sodoku solving programme
import os


grid = [
    [0,0,8,0,0,5,9,0,0],
    [4,2,9,0,6,0,1,8,0],
    [5,0,1,0,0,8,0,7,4],
    [6,1,0,0,4,0,8,0,0],
    [0,5,0,0,0,0,6,0,9],
    [9,0,4,0,0,2,0,0,1],	
    [1,0,6,0,8,0,7,5,0],	
    [7,4,0,0,0,0,0,1,0],	
    [0,0,0,0,0,7,4,9,6]	
	]

def print_grid(grid):
    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col

    return False


def solve_grid(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve_grid(grid):
                return True

            grid[row][col] = 0

    return False


def check_valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num: #and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num: #and pos[0] != i:
            return False

    # Check grid  3x3 box
    grid3x3_x = pos[1] // 3
    grid3x3_y = pos[0] // 3

    for i in range(grid3x3_y*3, grid3x3_y*3 + 3):
        for j in range(grid3x3_x * 3, grid3x3_x*3 + 3):
            if grid[i][j] == num: #and (i,j) != pos:
                return False

    return True

# Triggering Code
# clear the terminal screen
os.system('clear') 

# clear some space
print("\n\n")
# Print title
print("Puzzle Grid")
print("\n")
# print the puzzle grid

print_grid(grid)

# solve the grid

solve_grid(grid)

print("\n\n")
# Print title
print("Solution Grid")
print("\n")
# print the completed grid
print_grid(grid)
print("\n\n")
print("\n\n")
