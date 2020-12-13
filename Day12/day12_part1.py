#!/usr/bin/env python3

import os
import sys


def move_ship(data):
    DIRS = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    lat = 0
    long = 0
    dir = 90
    for command in data:
        letter = command[0]
        num = int(command[1:])
        # If the command is to go forward, go in the current direction
        if letter == 'F':
            letter = DIRS[dir]
        # Move or rotate as ordered
        if letter == 'N':
            long += num
        elif letter == 'S':
            long -= num
        elif letter == 'E':
            lat += num
        elif letter == 'W':
            lat -= num
        elif letter == 'L':
            dir = (dir - num) % 360
        elif letter == 'R':
            dir = (dir + num) % 360
        print('command:', command, 'dir:', dir, 'lat:', lat, 'long', long)
    print('manhattan distance:', abs(lat) + abs(long))


if __name__ == '__main__':
    # Get the absolute path of the current script
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    # Check for flags
    if '-t' in sys.argv:
        filename = 'test_input'
    else:
        filename = 'input'
    with open(os.path.join(__location__, filename)) as f:
        # Read file into list of strings, one string per line
        data = [line.rstrip('\n') for line in f]
    move_ship(data)
