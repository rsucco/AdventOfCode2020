#!/usr/bin/env python3

import os
import sys
import itertools


# Parses and validates the passports
def validate_passports(raw_passports):
    valid_passports = 0
    REQUIRED_FIELDS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    # Unfortunately, this seems to be the least unpythonic way to split a list based on an element deliminter
    # At the very least, it's the most pythonic way to do it that I could find in 15 minutes on StackOverflow
    # Blank lines separate passwords, so a string consisting solely of '\n' is the delimiter
    passports = [list(y) for x, y in itertools.groupby(
        raw_passports, lambda z: z == '\n') if not x]
    # Make sure the passport contains all of the required fields
    for passport in passports:
        passport = ''.join(passport).replace('\n', ' ').rstrip()
        if all([field in passport for field in REQUIRED_FIELDS]):
            valid_passports += 1
            print(passport, 'is a valid passport', '\n-----')
    return valid_passports


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
    print(validate_passports(data))
