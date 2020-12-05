#!/usr/bin/env python3

import os
import sys

# Figure out how many trees we bonk our toboggan into


def find_trees(tree_grid, slope):
    width = len(tree_grid[0])
    height = len(tree_grid)
    x = 0
    y = 0

    trees_hit = 0
    while y < height:
        x += slope[0]
        y += slope[1]
        # Loop around if necessary
        x %= width
        # If the list index is out of bounds, there's obviously not a tree there. This will allow slopes where ΔY > 1
        try:
            if tree_grid[y][x] == '#':
                trees_hit += 1
        except Exception:
            pass
    return trees_hit


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
    # Technically this should be (3, -1) since the Y coordinates are decreasing as you go down, but this makes list indexes easier to manage
    SLOPE = (3, 1)
    print('Total trees hit:', find_trees(data, SLOPE))
