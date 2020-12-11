#!/usr/bin/env python3

import os
import sys
import itertools
import re


# Validates the fields in the passport
def validate_fields(raw_passport):
    # Convert the key-value pairs to a dictionary
    passport = dict(
        map(lambda field: field.split(':'), raw_passport.split(' ')))
    # Yes, I know this could be one extremely long return statement, but I decided to err on the side of readability
    # Validate birth year
    if not (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
        return False
    # Validate issue year
    if not (int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
        return False
    # Validate expiration year
    if not (int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
        return False
    # Validate height
    height = int(
        ''.join(digit for digit in passport['hgt'] if digit.isdigit()))
    if not (('cm' in passport['hgt'] and height >= 150 and height <= 193) or
            ('in' in passport['hgt'] and height >= 59 and height <= 76)):
        return False
    # Validate hair color
    hcl_regex = re.compile('#[0-9a-f]{6}')
    if hcl_regex.match(passport['hcl']) is None:
        return False
    # Validate eye color
    EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passport['ecl'] not in EYE_COLORS:
        return False
    # Validate passport ID
    pid_regex = re.compile('[0-9]{9}')
    if pid_regex.match(passport['pid']) is None or len(passport['pid']) != 9:
        return False
    # Validate country ID
    # lmao just kidding, can you imagine
    return True


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
        if all([field in passport for field in REQUIRED_FIELDS]) and validate_fields(passport):
            valid_passports += 1
            print(passport, 'is a valid passport', '\n-----')
        else:
            print(passport, 'is an invalid passport womp womp', '\n-----')
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
