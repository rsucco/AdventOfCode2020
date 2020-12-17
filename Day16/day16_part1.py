#!/usr/bin/env python3

import os
import sys
import itertools


def get_scanning_error_rate(nearby_tickets, valid_values):
    return sum([int(value) for nearby_ticket in nearby_tickets
                for value in nearby_ticket if int(value) not in valid_values])


def get_all_valid_values(field_values):
    all_valid_values = set()
    for field in field_values:
        field = field.split(': ')[1]
        for value in field.split(' or '):
            range_boundaries = [int(num) for num in value.split('-')]
            for i in range(range_boundaries[0], range_boundaries[1] + 1):
                all_valid_values.add(i)
    return all_valid_values


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
        data = [line.rstrip('\n') for line in f]
    field_values, your_ticket, nearby_tickets = [list(y) for x, y in itertools.groupby(
        data, lambda z: z == '') if not x]
    valid_values = get_all_valid_values(field_values)
    nearby_tickets = [nearby_ticket.split(',')
                      for nearby_ticket in nearby_tickets[1:]]
    print('scanning error rate:',
          get_scanning_error_rate(nearby_tickets, valid_values))
