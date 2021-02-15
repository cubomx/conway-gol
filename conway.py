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
from matplotlib.image import AxesImage as image
from saveData import *

ON = 255
OFF = 0
vals = [ON, OFF]

file_ = None

X = 0
Y = 0
step = 0

def randomGrid(N: int):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def read_config(filename:str):
    global X
    global Y
    grid = np.zeros(X*Y).reshape(X, Y)

    
    # first, check if the directory of the file exists
    if exists(filename):
        file_ = open(filename, "r")
        print(type(file_))
        for idx, x in enumerate(file_):
            
            if idx == 0:
                # getting the size of the universe
                dims = x.split(" ")
                X = int(dims[0])
                Y = int(dims[1])
                grid = np.zeros(X*Y).reshape(X, Y)
            else:
                fig = x.split()
                start_x = int(fig[0])
                start_y = int(fig[1])
                type_ = find_pattern(fig[2])
                print(fig[2] + "hola")
                if type(type_) == np.ndarray: # checking if the pattern name exists

                    print("hei")
                    fig_x = type_.shape[0]
                    fig_y = type_.shape[1]
                    add_pattern(grid, type_, start_x, start_y, X, Y, fig_x, fig_y)
                    
    print("X: {0} {1}".format(X, Y))
    file_.close()
    return grid


def update(frameNum:int, img:image, grid:np.ndarray, N: int):
    global X, Y, step
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()

    cells = count_cells(grid, X, Y)

    step += 1
    
    newGrid = first_rule(grid, newGrid, N)

    if step <= 200:
        saveData(step, cells, file_)
    if step == 201:
        close_file(file_)

    
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    global file_
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
   


    
    
    # set grid size
    grid = None
        
    # set animation update interval
    updateInterval = 50
    if len(sys.argv) > 1:
        print("Filename is: ", sys.argv[1]) 
        grid = read_config(sys.argv[1])
        
    else:
        grid = randomGrid(X)
    
    print("X: {0} {1},, {2} {3}".format(X, Y, grid.shape[0], grid.shape[1]))

    file_ = create_file("data.txt")

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    print(type(img))
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, X),
                                  frames = 100,
                                  interval=200,
                                  save_count=100)

    plt.show()

# call main
if __name__ == '__main__':
    main()
