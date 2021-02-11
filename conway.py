"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from os.path import exists
from rules import *
from pattern import *

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N: int):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def read_config(filename:str):
    X = 10
    Y = 10
    grid = np.zeros(X*Y).reshape(X, Y)

    
    
    

    if exists(filename):
        file_ = open(filename, "r")
        for idx, x in enumerate(file_):
            if idx == 0:
                dims = x.split(" ")
                X = int(dims[0])
                Y = int(dims[1])
                grid = np.zeros(X*Y).reshape(X, Y)
            else:
                fig = x.split(" ")
                start_x = int(fig[0])
                start_y = int(fig[1])
                type_ = find_pattern(fig[2])
                if type_ is not None:
                    fig_x = type_.shape[0]
                    fig_y = type_.shape[1]
                    print(fig_x, fig_y)
                    add_pattern(grid, type_, start_x, start_y, X, Y, fig_x, fig_y)
        
    file_.close()
    return grid

def addGlider(i:int, j:int, grid:np.ndarray):
    """adds a glider with top left cell at (i, j)"""
    
    grid[i:i+3, j:j+3] = glider

def update(frameNum:int, img, grid:np.ndarray, N: int):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life

    newGrid = first_rule(grid, newGrid, N)
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
   


    
    
    # set grid size
    X = 100
    Y = 100
        
    # set animation update interval
    updateInterval = 50
    if len(sys.argv) > 1:
        print("Filename is: ", sys.argv[1]) 
        grid = read_config(sys.argv[1])
    else:
        grid = randomGrid(X)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, X, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()

# call main
if __name__ == '__main__':
    main()
