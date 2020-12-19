#!/usr/bin/env python3

import os
import sys


class Expression:
    def __init__(self):
        super().__init__()


def evaluate_expression(numbers, operators, total=0):
    new_operators = []
    new_numbers = []
    print(numbers, operators)
    for number, operator, i in zip(numbers, operators, range(len(numbers))):
        if '(' in number:
            # Here I want to call this same function again recursively, but with the current num and op stripped
            # Strip the opening parenthesis of the number before sending it down the pipe
            numbers[i] = numbers[i][1:]
            return evaluate_expression(numbers, operators, 0)
        elif ')' in number:
            # Here I want to return the values from inside the parenthesis and strip one parenthesis from the number
            return
        else:
            if operator == '+':
                return total + int(number)
            elif operator == '*':
                return total * int(number)

    # for number, operator, i in zip(numbers, operators, range(len(numbers))):
    #     if operator == 'END':

    #     # Begin subexpression if number has a '(' in it
    #     # if '(' in number:

    #     if not any(char in number for char in ['(', ')']):
    #         if operator == '+':
    #             total += int(number)
    #         elif operator == '-':
    #             total -= int(number)
    #         elif operator == '/':
    #             total /= int(number)
    #         elif operator == '*':
    #             total *= int(number)
    #         print(number, operator, total)
        # else:
        #     print(line)
        #     print(number, operator, i)
        #     print(line[i + 2:])
        #     break


def evaluate_line(line):
    print(line)
    line = line.split(' ')
    # Need an implicit addition from 0 for the first number
    line.insert(0, '+')
    # Every equation alternates between numbers (with or without paraenthesis), and operators
    numbers = [line[num] for num in range(1, len(line), 2)]
    operators = [line[num] for num in range(0, len(line), 2)]
    print([number + ' ' + operator for number,
           operator in zip(numbers, operators)])
    evaluate_expression(numbers, operators)


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
    for line in data:
        evaluate_line(line)
        print('======')

    test = ['1', '+', '2', '*', '3', '+', '4', '*', '5', '+', '6']
