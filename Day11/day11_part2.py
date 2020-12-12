#!/usr/bin/env python3

import os
import sys
import itertools


class Seat:
    def __init__(self, char):
        self.char = char
        # '.' for floor, '#' for occupied seat, 'L' for empty seat
        if char == '.':
            self.floor = True
        else:
            self.floor = False
        if char == '#':
            self.occupied = True
        else:
            self.occupied = False

    def __str__(self):
        return self.char

    def copy(self):
        return Seat(str(self))


def create_grid(data):
    grid = []
    for line in data:
        row = [Seat(char) for char in line]
        grid.append(row)
    return grid


# I want it to be clear that I am not at all proud of how I wrote this
# It does have an interesting lovecraftian organic feel to it though
def update_grid(grid):
    def get_num_occupied(x, y):
        # Get the eight different slopes to search along, in the form of (x increment, y increment)
        slopes = set(itertools.permutations([0, 1, 1, -1, -1], 2))
        # Search each slope until we encounter a seat or run out of bounds
        num_occupied = 0
        for slope in slopes:
            check_x = x + slope[0]
            check_y = y + slope[1]
            while check_x >= 0 and check_x < len(grid[0]) and check_y >= 0 and check_y < len(grid):
                if not grid[check_y][check_x].floor:
                    if grid[check_y][check_x].occupied:
                        num_occupied += 1
                    break
                check_x += slope[0]
                check_y += slope[1]
        return num_occupied

    new_grid = []
    for y, row in enumerate(grid):
        new_row = []
        for x, seat in enumerate(row):
            # But floor... floor never changes
            if not seat.floor:
                num_occupied = get_num_occupied(x, y)
                # Too crowded, time to peace out
                if seat.occupied and num_occupied >= 5:
                    new_seat = Seat('L')
                # Hell yeah, legroom, I'm gonna sit in this seat
                elif not seat.occupied and num_occupied == 0:
                    new_seat = Seat('#')
                else:
                    new_seat = seat.copy()
            else:
                new_seat = Seat('.')
            new_row.append(new_seat)
        new_grid.append(new_row)
    return new_grid


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_grid(grid):
    text_grid = ''
    for row in grid:
        text_grid += ''.join(str(seat) for seat in row) + '\n'
    return text_grid


def fill_seats(grid):
    previous_grid = ''
    while print_grid(grid) != previous_grid:
        clear()
        print(print_grid(grid))
        previous_grid = print_grid(grid)
        grid = update_grid(grid)
    return grid


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
    grid = create_grid(data)
    grid = fill_seats(grid)
    num_filled = sum(seat.occupied for seat in itertools.chain(*grid))
    print('Total seats filled:', num_filled)
