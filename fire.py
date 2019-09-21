# Annie Gao
# CSc 110, Spring 2018, Section 1B
# HW 10: Fire
# Completed: 11/15/17
# hours worked: 4

# This program simulates a fire spreading in 4 directions based on
# the propagation possibility. 

from DrawingPanel import *
from random import *

PROPAGATION = 75    # percentage chance that the fire spreads

# This function opens a file and calls several functions to create a grid
# given the file information. The while loop is exited when no fire is left. 
def main():
    file_name = input("File name? ")
    lines = open(file_name).readlines()
    p = DrawingPanel(10*len(lines[0].split()), 10*len(lines))

    grid = organize(lines)
    draw(p, grid)
    fire = True
    while fire == True:
        grid = spread(grid)
        draw(p, grid)
        fire = stop_or_go(grid)
        p.sleep(100)

# This function creates the initial grid with information from the given file.
def organize(lines):
    grid = []
    for i in range(len(lines)):
        line = lines[i].strip().split()
        grid.append(line)

    return grid

# This function draws the panel of empty, tree, and fire squares.
def draw(p, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos = int(grid[i][j])
            if pos == 1:
                color = "green"
            elif pos == 2:
                color = "red"
            else:
                color = "yellow"
            p.fill_rect(10*i,10*j, 10,10, color)

# This function creates a new grid to replace the previous one,
# demonstrating any changes that occur when the fire spreads.
def spread(grid):
    new_grid = []
    for i in range(len(grid)):
        grid_line = []
        for j in range(len(grid[i])):
            pos = grid[i][j]    # position
            if pos == "1":      # tree
                north = grid[i-1][j]
                east = grid[i][j+1]
                south = grid[i+1][j]
                west = grid[i][j-1]
                poss_fire = randint(1,100)
                if north == "2" and poss_fire < PROPAGATION:
                    pos = "2"
                elif east == "2" and poss_fire < PROPAGATION:
                    pos = "2"
                elif south == "2" and poss_fire < PROPAGATION:
                    pos = "2"
                elif west == "2" and poss_fire < PROPAGATION:
                    pos = "2"

            elif pos == "2":
                pos = "0"
                
            grid_line.append(pos)       # whether or not change was made, saved
        new_grid.append(grid_line)

    return new_grid

# This function tests if there are any fires left.
def stop_or_go(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos = grid[i][j]
            if pos == "0" or pos == "1":    # to test if any fire squares remain
                count += 1
                
    # count = num squares --> no fire left, returns False 
    return count != len(grid)*len(grid[0])

main()
