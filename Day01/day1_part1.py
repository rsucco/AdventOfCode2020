#!/usr/bin/env python3

import itertools

# Find two numbers that sum to 2020, then multiply them and return the result
def find_2020(content):
    for x, y in itertools.combinations(content, 2):
        if x + y == 2020:
            return x * y

if __name__ == '__main__':
    # Read file into list of strings, one string per line
    with open('./input') as f:
        content = [int(line.rstrip('\n')) for line in f]
    print(find_2020(content))