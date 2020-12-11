#!/usr/bin/env python3

import os
import sys
import itertools


# Get a list of lists, each list being a group of people
def get_groups(data):
    return [list(y) for x, y in itertools.groupby(
        data, lambda z: z == '\n') if not x]


# Count the number of questions for which at least one person in the group said 'yes'
def count_answers(group):
    unique_answers = set(''.join(group))
    unique_answers.discard('\n')
    return len(unique_answers)


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
        total_answers += count_answers(group)
    print('Total \'yes\' answers:', total_answers)
