#!/usr/bin/env python3

import os
import sys


def speak_numbers(data, stopping_point):
    spoken_nums = [int(num) for num in data.split(',')]
    for turn in range(len(spoken_nums) + 1, stopping_point + 1):
        if spoken_nums[-1] not in spoken_nums[:-1]:
            spoken_nums.append(0)
        else:
            # Get the index of the penultimate occurance of the number in the list
            for i in reversed(range(len(spoken_nums) - 1)):
                if spoken_nums[i] == spoken_nums[-1]:
                    spoken_nums.append(len(spoken_nums) - 1 - i)
                    break
        print('turn', turn)
        print('last spoken:', spoken_nums[-2])
        print('speaking:', spoken_nums[-1])
        print('=============')


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
        data = f.readline()
    speak_numbers(data, 2020)
