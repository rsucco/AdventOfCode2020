#!/usr/bin/env python3

import re

# Validate that a password meets the policy standards at the time it was created
def validate_password(password_raw):
    # Split the password string on 3 delimiters ('-', ' ', or ': ') to get four strings: two positions, char, and password
    # RegEx might not be the most pythonic way to do this, but I wanted some practice and damn if they aren't concise
    password_data = re.split('-|\s|:\s', password_raw)
    # Assign readable names to the four substrings, and correct for the fact that the dumbass toboggan company uses index 1
    POS1 = int(password_data[0]) - 1
    POS2 = int(password_data[1]) - 1
    CHAR = password_data[2]
    PASS = password_data[3]
    # Make sure that one and only one of the positions specified matches the specified character
    return (PASS[POS1] == CHAR) ^ (PASS[POS2] == CHAR)

if __name__ == '__main__':
    # Read file into list of strings, one string per line
    with open('./input') as f:
        data = [line.rstrip('\n') for line in f]

    valid_passwords = 0
    for password in data:
        if validate_password(password):
            print(password.split(': ')[-1], 'is a valid password.')
            valid_passwords += 1
    print('There are a total of', valid_passwords, 'valid passwords.')