import numpy as np

beehive = np.array([[0,    255, 255, 0], 
                       [255,  0, 0, 255], 
                       [0, 255, 255, 0]])

block = np.array([[255, 255],
                    [255, 255]])

glider = np.array([[0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])

spaceship_4 = np.array([[0, 255, 255, 0, 0],
                        [255, 255, 255, 255, 0],
                        [255, 255, 0, 255, 255],
                        [0, 0, 255, 255, 0]])


blinker = np.array([[255], [255], [255]])

toad = np.array([[0, 255, 255, 255],
                    [255, 255, 255, 0]])

beacon = np.array([[255, 255, 0, 0],
                    [255, 255, 0, 0],
                    [0, 0, 255, 255],
                    [0, 0, 255, 255]])

loaf = np.array([[0, 255, 255, 0],
                    [255, 0, 0, 255],
                    [0, 255, 0, 255],
                    [0, 0, 255, 0]])

boat = np.array([[255, 255, 0],
                    [255, 0, 255],
                    [0, 255, 0]])

tub = np.array([[0, 255, 0],
                [255, 0, 255],
                [0, 255, 0]])



    

pattern = {"beehive": beehive, "block":block, "glider":glider, "spaceship_4":spaceship_4, "blinker":blinker,
"toad":toad, "beacon":beacon, "loaf":loaf, "boat":boat, "tub":tub}

''' Adding the pattern to the grid if possible'''

def add_pattern(grid:np.ndarray, array:np.ndarray, start_x:int, start_y:int, limit_x:int, limit_y:int, fig_x:int, fig_y:int):
    " Checking if the figure is not out of range"
    if start_x + fig_x < limit_x:
        if start_y + fig_y < limit_y:
            # Adding every spot of the pattern into the grid
            for i in range(start_x, start_x+fig_x):
                for j in range(start_y, start_y+fig_y):
                    idx = i - start_x
                    idy = j - start_y
                    grid[i, j] = array[idx, idy]
        else:
            return False
    else:
        return False

''' Checking if the pattern given by the configuration
    exists in our pattern database above.
'''
def find_pattern(name:str):
    return pattern.get(name)
    