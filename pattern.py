import numpy as np

beehive = np.array([[0,    255, 255, 0], 
                       [255,  0, 0, 255], 
                       [0, 255, 255, 0]])

block = np.array([[255, 255],
                    [255, 255]])

pattern = {"beehive": beehive, "block":block}


def add_pattern(grid, array, start_x, start_y, limit_x, limit_y, fig_x, fig_y):
    if start_x + fig_x < limit_x:
        if start_y + fig_y < limit_y:
            grid[start_x:start_x+fig_x, start_y:start_y+fig_y] = array
            for i in range(start_x, start_x+fig_x):
                for j in range(start_y, start_y+fig_y):
                    idx = i - start_x
                    idy = j - start_y
                    grid[i, j] = array[idx, idy]
        else:
            return False
    else:
        return False

def find_pattern(name):
    if name in pattern.keys():
        return pattern[name]
    return None
    