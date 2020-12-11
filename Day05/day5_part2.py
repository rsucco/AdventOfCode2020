#!/usr/bin/env python3

import os
import sys


# Get the row number from the boarding pass
def get_row(boarding_pass):
    row_info = boarding_pass[:7]
    possible_rows = range(0, 128)
    for row_char in row_info:
        # The row_char will specify whether to take the top half or the bottom half
        split_point = int(len(possible_rows) / 2)
        if row_char == 'F':
            # For the last char, return the correct value
            if len(possible_rows) <= 2:
                return possible_rows[0]
            # For any of the other chars, split the list along the split point
            else:
                possible_rows = possible_rows[:split_point]
        else:
            if len(possible_rows) <= 2:
                return possible_rows[-1]
            else:
                possible_rows = possible_rows[split_point:]
    # Return -1 as an error signal if the row couldn't be calculated
    return -1


# Works the same as get_row and I really should combine them but I'm not going to unless I have to revisit this for a future puzzle
def get_column(boarding_pass):
    column_info = boarding_pass[7:]
    possible_columns = range(0, 8)
    for column_char in column_info:
        split_point = int(len(possible_columns) / 2)
        if column_char == 'L':
            if len(possible_columns) <= 2:
                return possible_columns[0]
            else:
                possible_columns = possible_columns[:split_point]
        else:
            if len(possible_columns) <= 2:
                return possible_columns[1]
            else:
                possible_columns = possible_columns[split_point:]
    return -1


def get_seat_id(row, column):
    return row * 8 + column


# Find the only empty seat within the range of seat IDs
def find_my_seat(data):
    all_seat_ids = []
    for boarding_pass in data:
        all_seat_ids.append(get_seat_id(
            get_row(boarding_pass), get_column(boarding_pass)))
    missing_seat_ids = []
    for i in range(min(all_seat_ids), max(all_seat_ids)):
        if i not in all_seat_ids:
            missing_seat_ids.append(i)
    return missing_seat_ids


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
    print('Missing seat ID:', find_my_seat(data)[0])
