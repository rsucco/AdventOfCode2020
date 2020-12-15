#!/usr/bin/env python3

import os
import sys
import itertools


class Instruction:
    def __init__(self, data):
        self.mask = data[0].split(' = ')[1]
        self.instructions = []
        for instruction in data[1:]:
            addresses = self.apply_mask(
                int(instruction.split('[')[1].split(']')[0]))
            value = int(instruction.split(' = ')[1])
            self.instructions.append((addresses, value))

    def __str__(self):
        return 'mask: ' + str(self.mask) + ' | values: ' + ', '.join(str(instruction) for instruction in self.instructions)

    def apply_mask(self, num):
        # Always 36 bits, big-endian, so pad to 36 characters with 0's after converting to binary with an f-string
        binary_num = f'{num:08b}'.zfill(36)
        # Take the original number's bit if the mask has an 'X', otherwise take the mask's value
        new_binary_nums = ['']
        for i in range(36):
            if self.mask[i] == '0':
                new_binary_nums = [new_binary_num + binary_num[i]
                                   for new_binary_num in new_binary_nums]
            elif self.mask[i] == '1':
                new_binary_nums = [new_binary_num +
                                   '1' for new_binary_num in new_binary_nums]
            # Floating
            else:
                split_nums = []
                for new_binary_num in new_binary_nums:
                    split_nums.append(new_binary_num + '0')
                    split_nums.append(new_binary_num + '1')
                new_binary_nums = split_nums[:]
        # Convert back to base-10 integers
        return [int(new_binary_num, 2) for new_binary_num in new_binary_nums]

    def execute(self, update_memory):
        for addresses, value in self.instructions:
            for address in addresses:
                update_memory(address, value)


class DockBoi:
    def __init__(self, program):
        self.memory = {}
        self.program = self.load_program(program)

    def __str__(self):
        return str(self.memory)

    # Callback for the instruction to use
    def update_memory(self, address, value):
        self.memory[address] = value

    def load_program(self, program):
        instructions = []
        for instruction in program:
            # 'mask = ' signals the beginning of a new instruction
            if 'mask = ' in instruction:
                instructions.append([])
            instructions[-1].append(instruction)
        # Buffalo buffalo Buffalo buffalo
        #                buffalo buffalo Buffalo buffalo
        instructions = [Instruction(instruction)
                        for instruction in instructions]
        return instructions

    def run_program(self):
        for instruction in self.program:
            # Pass the update memory callback so the instruction can do its thang
            instruction.execute(self.update_memory)

    def sum_values(self):
        return sum(self.memory.values())


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
    db = DockBoi(data)
    print(db)
    db.run_program()
    print(db)
    print(db.sum_values())
