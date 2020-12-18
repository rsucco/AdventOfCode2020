#!/usr/bin/env python3

import os
import sys
import itertools


def get_all_valid_values(field_values):
    all_valid_values = {}
    for field in field_values:
        field_name, field = field.split(': ')
        field_valid_values = set()
        # Add the possible valid values to a set for each field
        for value in field.split(' or '):
            range_boundaries = [int(num) for num in value.split('-')]
            for i in range(range_boundaries[0], range_boundaries[1] + 1):
                field_valid_values.add(i)
        all_valid_values[field_name] = field_valid_values
    return all_valid_values


def get_field_possibilities(nearby_tickets, all_valid_values):
    columns = []
    for i in range(len(nearby_tickets[0])):
        column = []
        for nearby_ticket in nearby_tickets:
            column.append(nearby_ticket[i])
        columns.append(column)

    possible_field_indices = {}

    for i,

    for column in columns:
        if all(num in all_valid_values for num in column):
            possible_field_indices[]

    # for i in range(len(nearby_tickets[0])):
    #     for field_name, valid_values in all_valid_values.items():
    #         for nearby_ticket in nearby_tickets:
    #             print(nearby_ticket[i])
    #         input()

    #         if all((int(nearby_ticket[i]) in valid_values) for nearby_ticket in nearby_tickets):
    #             if field_name not in possible_field_indices:
    #                 possible_field_indices[field_name] = [i]
    #             else:
    #                 possible_field_indices[field_name].append(i)

    # for valid in all_valid_values.items():
    #     print(valid)
    # print('possible indices:', possible_field_indices)
    return possible_field_indices


def deduce_fields(field_possibilities):
    confirmed_field_indices = {}
    # Sort the dictionary to start with the most narrowed-down fields
    field_possibilities = dict(sorted(field_possibilities.items(),
                                      key=lambda item: len(item[1])))
    updated_field_possibilities = field_possibilities.copy()
    print((updated_field_possibilities))
    while len(confirmed_field_indices) < len(field_possibilities):
        # print(len(field_possibilities) -
        #       len(confirmed_field_indices), 'more fields to deduce')
        # print('confirmed so far:', confirmed_field_indices)
        for field, possibilities in field_possibilities.items():
            possibilities = [possibility for possibility in possibilities
                             if possibility not in confirmed_field_indices.values()]
            if len(possibilities) == 1:
                print('deduced field', field, 'at index', possibilities[0])
                confirmed_field_indices[field] = possibilities[0]
                for field, possibilities in field_possibilities.items():
                    updated_field_possibilities[field] = [possibility for possibility in possibilities
                                                          if possibility not in confirmed_field_indices.values()]

        field_possibilities = updated_field_possibilities.copy()
        print(field_possibilities)
        input()

        # print(confirmed_field_indices)
        # print('poss', field_possibilities)
        # print('updated', updated_field_possibilities)
        # break
    return confirmed_field_indices


def translate_ticket(ticket, field_indices):
    translated_ticket = {}
    for field, index in field_indices.items():
        translated_ticket[field] = ticket[index]
    return translated_ticket


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
    field_values, your_ticket, nearby_ticket_strs = [list(y) for x, y in itertools.groupby(
        data, lambda z: z == '') if not x]
    nearby_tickets = []
    for nearby_ticket in nearby_ticket_strs[1:]:
        nearby_tickets.append([int(value)
                               for value in nearby_ticket.split(',')])

    your_ticket = [int(value) for value in your_ticket[1].split(',')]

    valid_values = get_all_valid_values(field_values)
    field_possibilities = get_field_possibilities(nearby_tickets, valid_values)
    print(field_possibilities)
    sys.exit()
    confirmed_field_indices = deduce_fields(field_possibilities)
    translated_ticket = translate_ticket(your_ticket, confirmed_field_indices)
