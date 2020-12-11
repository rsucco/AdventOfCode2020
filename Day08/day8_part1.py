#!/usr/bin/env python3

import os
import sys
import time


class Instruction:
    def __init__(self, operation='nop', argument=0):
        self.operation = operation
        self.argument = int(argument)

    # Return a tuple with the updated acculator and pointer values after running the given instruction
    def execute(self, accumulator, pointer):
        # 'nop' increments the pointer and returns control
        if self.operation == 'nop':
            return (accumulator, pointer + 1)
        # 'acc' increments the accumator by the integer value specified and increments the pointer by 1
        elif self.operation == 'acc':
            return (accumulator + self.argument, pointer + 1)
        # 'jmp' increments the pointer by the integer value specified
        elif self.operation == 'jmp':
            return (accumulator, pointer + self.argument)
        # Do NOT fail gracefully
        else:
            raise Exception('Invalid instruction')

    # For debugging
    def __str__(self):
        return self.operation + ' ' + str(self.argument)


class GameBoi:
    def __init__(self, program=[()]):
        self.program = program
        self.accumulator = 0
        self.pointer = 0

    def load_program(self, code):
        self.program = []
        for line in code:
            operation, argument = line.split(' ')
            self.program.append(Instruction(operation, argument))

    def run_program(self, no_repeats=False):
        start_time = time.time()
        print('program start')
        print(str(self))
        visited_indices = []
        total_instructions = 0
        # Run as long as a valid instruction is referenced
        while self.pointer < len(self.program):
            print('instruction:', self.program[self.pointer])
            if no_repeats:
                visited_indices = sorted(visited_indices)
                print(visited_indices)
                if self.pointer in visited_indices:
                    print('infinite loop detected, terminating')
                    print(str(self))
                    break
                visited_indices.append(self.pointer)
            self.accumulator, self.pointer = self.program[self.pointer].execute(
                self.accumulator, self.pointer)
            total_instructions += 1
            print(str(self))
        print('total instructions executed:', total_instructions)
        print('execution completed in', time.time() - start_time, 'seconds')
        print('have a nice day')

    def __str__(self):
        return 'acc:' + str(self.accumulator) + '| pnt:' + str(self.pointer) + '\n----'


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

    gb = GameBoi()
    gb.load_program(data)
    gb.run_program(no_repeats=True)
