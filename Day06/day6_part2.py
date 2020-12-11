#!/usr/bin/env python3

import os
import sys
import itertools
import string


# Get a list of lists, each list being a group of people
def get_groups(data):
    return [list(y) for x, y in itertools.groupby(
        data, lambda z: z == '\n') if not x]


# Count the number of questions for which everyone in the group said 'yes'
def count_unanimous_answers(group):
    group = [person.rstrip('\n') for person in group]
    unanimous_answers = 0
    for letter in string.ascii_lowercase:
        if all(letter in person for person in group):
            unanimous_answers += 1
    return unanimous_answers


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
        data = [line for line in f]
    groups = get_groups(data)
    total_answers = 0
    for group in groups:
        total_answers += count_unanimous_answers(group)
    print('Total unanimous \'yes\' answers:', total_answers)
