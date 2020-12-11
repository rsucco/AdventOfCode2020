#!/usr/bin/env python3

import os
import sys


def get_adapters(data):
    adapters = list(sorted(int(datum) for datum in data))
    # The wall starts at 0 jolts
    adapters.insert(0,0)
    # The device's built-in adapter is always 3 higher than the highest
    adapters.append(max(adapters) + 3)
    return adapters

def get_joltage_distribution(data):
    adapters = get_adapters(data)
    joltage_count = 0
    joltage_distribution = {}
    for i in range(1, len(adapters)):
        difference = adapters[i] - adapters[i - 1]
        if difference in joltage_distribution.keys():
            joltage_distribution[difference] += 1
        else:
            joltage_distribution[difference] = 1
        joltage_count += difference
    return joltage_distribution

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
    distributions = get_joltage_distribution(data)
    print(distributions[1] * distributions[3])
