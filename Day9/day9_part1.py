#!/usr/bin/env python3

import os
import sys
import itertools


def validate_number(num, previous_nums):
    return any(x + y == num for x, y in itertools.combinations(previous_nums, 2))


def find_outlier(preamble_size, data):
    for i, num in enumerate(data[preamble_size:], preamble_size):
        if not validate_number(num, data[i - preamble_size:i]):
            return num
    return 'none'


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
        data = [int(line.rstrip('\n')) for line in f]

    PREAMBLE_SIZE = 25
    print(find_outlier(PREAMBLE_SIZE, data))
