import numpy as np

def search_neighbors(grid:np.ndarray, new_grid:np.ndarray, i:int, j:int, N:int):
    quantity = 0
    state = grid[i, j]
    # first, check all 8 neighbor cells 
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if y == j and x == i:
                continue
            if x >= 0 and x < N:
                if y >= 0 and y < N:
                    if grid[x, y] == 255:
                        quantity += 1
    # check the rules applying to our system
    if state == 0:
        if quantity == 3:
            new_grid[i, j] = 255
    elif state == 255:
        if quantity > 3 or quantity < 2:
            new_grid[i, j] = 0



def first_rule(grid:np.ndarray, new_grid:np.ndarray, N:int):
    for i in range (N):
        for j in range(N):
            # check the rules for the survival of every cell
            search_neighbors(grid, new_grid, i, j, N)
    return new_grid
            


