#!/usr/bin/env python3

import os
import sys


# Figure out how many trees we bonk our toboggan into
def find_trees(tree_grid, slopes):
    width = len(tree_grid[0])
    height = len(tree_grid)

    # Since we multiply the running total by the new tree count for each slope, it needs to start at 1 instead of 0
    running_total = 1
    for slope in slopes:
        print('Slope:', slope)
        trees_hit = 0
        x = 0
        y = 0
        while y < height:
            x += slope[0]
            # Loop around if necessary
            if x > width - 1:
                x = x % width
            y += slope[1]
            # If the list index is out of bounds, there's obviously not a tree there. This will allow slopes where ΔY > 1
            try:
                if tree_grid[y][x] == '#':
                    trees_hit += 1
            except Exception:
                pass
        print('Trees hit:', trees_hit)
        running_total *= trees_hit
    return running_total


if __name__ == '__main__':
    # Get the absolute path of the current script
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    # Accept an input file name if passed on the command line; otherwise just use 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'input'
    with open(os.path.join(__location__, filename)) as f:
        # Read file into list of strings, one string per line
        data = [line.rstrip('\n') for line in f]
    # Technically the Y slope values should be negative since the Y coordinates are decreasing as you go down, but this makes list indexes easier to manage
    SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print('Multiplied trees from all slopes:', find_trees(data, SLOPES))
