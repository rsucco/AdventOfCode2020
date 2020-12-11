#!/usr/bin/env python3

import itertools

# Find three numbers that sum to 2020, then multiply them and return the result
def find_2020(content):
    for x, y, z in itertools.combinations(content, 3):
        if x + y + z == 2020:
            return x * y * z

if __name__ == '__main__':
    # Read file into list of strings, one string per line
    with open('./input') as f:
        content = [int(line.rstrip('\n')) for line in f]
    print(find_2020(content))