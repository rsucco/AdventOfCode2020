#!/usr/bin/env python3

import os
import sys
import time


def speak_numbers(data, stopping_point):
    start_time = time.time()
    spoken_nums = [int(num) for num in data.split(',')]
    last_spoken = {num: [i, i] for i, num in enumerate(spoken_nums)}
    next_num = spoken_nums[-1]
    for turn in range(len(spoken_nums), stopping_point):
        previous_num = next_num
        next_num = last_spoken[previous_num][0] - last_spoken[previous_num][1]
        # Update the last spoken values for the last number
        if next_num in last_spoken:
            last_spoken[next_num][1] = last_spoken[next_num][0]
            last_spoken[next_num][0] = turn
        # Create new values if it's the first time
        else:
            last_spoken[next_num] = [turn, turn]
        # Print some data for debugging and sanity
        if turn % 10000 == 0:
            elasped = time.time() - start_time
            print('elasped time:', f'{elasped:.2f}', 'seconds')
            pace = turn / elasped
            total = stopping_point / pace
            print('pace:', f'{pace:.2f}', 'numbers/sec')
            print('estimated remaining time:',
                  f'{total - elasped:.2f}', 'seconds')
            print('=============')
    print('result:', next_num)


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
    speak_numbers(data, 30000000)
