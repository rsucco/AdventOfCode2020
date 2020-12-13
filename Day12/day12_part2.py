#!/usr/bin/env python3

import os
import sys


def move_ship(data):
    ship_lat = 0
    ship_long = 0
    wp_lat_offset = 10
    wp_long_offset = 1
    for command in data:
        letter = command[0]
        num = int(command[1:])
        # If the command is to go forward, go towards the waypoint the number of times specified
        if letter == 'F':
            ship_lat += wp_lat_offset * num
            ship_long += wp_long_offset * num
        # Move the waypoint as ordered
        elif letter == 'N':
            wp_long_offset += num
        elif letter == 'S':
            wp_long_offset -= num
        elif letter == 'E':
            wp_lat_offset += num
        elif letter == 'W':
            wp_lat_offset -= num
        elif letter == 'L':
            for i in range(int(num / 90)):
                wp_lat_offset, wp_long_offset = -wp_long_offset, wp_lat_offset
        elif letter == 'R':
            for i in range(int(num / 90)):
                wp_lat_offset, wp_long_offset = wp_long_offset, -wp_lat_offset
        print('command:', command, 'ship lat:', ship_lat, 'ship long:', ship_long,
              'waypoint lat offset:', wp_lat_offset, 'waypoint long offset:', wp_long_offset)
    print('manhattan distance:', abs(ship_lat) + abs(ship_long))


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
