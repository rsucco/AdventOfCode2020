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
    def __init__(self, program=[Instruction()], verbose=False, debug=False):
        self.program = program
        self.accumulator = 0
        self.pointer = 0
        self.verbose = verbose
        self.debug = debug
        self.EXIT_SUCCESS = 0
        self.EXIT_INVALID_POINTER = 1
        self.EXIT_INFINITE_LOOP = 2

    def load_program(self, code):
        self.program = []
        for line in code:
            operation, argument = line.split(' ')
            self.program.append(Instruction(operation, argument))

    def stdout(self, *text):
        if self.verbose:
            print(*text)

    def stderr(self, *text):
        if self.debug:
            print(*text)

    # Returns a tuple containing the accumulator value at the time of termination and the exit code
    def run_program(self, no_repeats=False):
        self.accumulator = 0
        self.pointer = 0
        start_time = time.time()
        self.stdout('program start')
        self.stderr(str(self))
        visited_indices = []
        total_instructions = 0
        # Run as long as a valid instruction is referenced
        try:
            while True:
                self.stderr('instruction:', self.program[self.pointer])
                if no_repeats:
                    visited_indices = sorted(visited_indices)
                    if self.pointer in visited_indices:
                        self.stdout(
                            'execution terminated unsuccessfully: infinite loop detected')
                        return (self.accumulator, self.EXIT_INFINITE_LOOP)
                    visited_indices.append(self.pointer)
                self.accumulator, self.pointer = self.program[self.pointer].execute(
                    self.accumulator, self.pointer)
                total_instructions += 1
                self.stderr(str(self))
                # Terminate if pointer is exactly 1 more than the end of the program
                if self.pointer == len(self.program):
                    self.stdout('execution terminated successfully')
                    self.stderr('total instructions executed:',
                                total_instructions)
                    self.stderr('execution completed in',
                                time.time() - start_time, 'seconds')
                    self.stdout('have a nice day')
                    return (self.accumulator, self.EXIT_SUCCESS)
        except IndexError:
            self.stdout('invalid pointer:', self.pointer)
            return (self.accumulator, self.EXIT_INVALID_POINTER)

    def __str__(self):
        return 'acc: ' + str(self.accumulator) + ' | pnt: ' + str(self.pointer) + '\n----'


# I've automated my normal debugging strategy of 'just try changing everything until something works'
# Returns a tuple containing a GameBoi that will actually execute successfully and the index that was changed
def find_good_program(code):
    gb = GameBoi()
    gb.load_program(code)
    # Get the indices of each jmp command so we can try replacing all of them
    jmp_indices = [i for i, instruction in enumerate(gb.program)
                   if instruction.operation == 'jmp']
    for j in jmp_indices:
        gb.load_program(code)
        gb.program[j].operation = 'nop'
        if gb.run_program(no_repeats=True)[1] == 0:
            return (gb, j)


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

    gb, j = find_good_program(data)
    gb.verbose = True
    print(gb.run_program(no_repeats=True)[0])
    print('changed index', j, 'from jmp to nop')
