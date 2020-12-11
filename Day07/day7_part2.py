#!/usr/bin/env python3

import os
import sys


class Bag:
    def __init__(self, name):
        self.name = name
        self.children = {}

    # Check if a bag is down somewhere in the rat's nest
    def holds(self, subbag):
        return any(child.name == subbag or child.holds(subbag) for child in self.children.keys())

    # Return the total number of bags that can be contained, Matryoshka-style (I promise I spelled that right first try without Google)
    def capacity(self):
        # Return the sum of the bags directly contained in this one, then tell the children to do likewise and add it all up
        # This is called 'recursion' (probably), thanks for coming to my Ted Talk
        return sum(self.children.values()) + sum(child.capacity() * count for child, count in self.children.items())

    def add_child(self, child, count = 1):
        if child in self.children:
            self.children[child] += count
        else:
            self.children[child] = count

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    # For debugging but leaving anyways
    def __str__(self):
        return '[' + self.name + ': ' + ' '.join(str(child) for child in self.children) + ']'


# Returns a neat list of child bags without their counts
def get_children(line):
    # Text after 'contain ' is the children, ' bag, ' is the delimiter, and the last six characters are the extraneous ' bags.'
    return line.replace('bags', 'bag').split('contain ')[1][:-5].split(' bag, ')

# Parse the input data into a dictionary of Bag objects
# I feel like this could've done been done with either a dict or a
# class, but I didn't know how so I just used both, and it's ugly, oops
def parse_bags(data):
    # Initialize the bag dictionary
    # Text before the first occurance of the word 'bags' is the name of the bag
    all_bags = {line.split(' bags')[0] : Bag(line.split(' bags')[0]) for line in data}
    # Add the child bags to the overall dictionary
    for line in data:
        # Don't want the numbers for this part
        for child in [child.split(' ', 1)[1] for child in get_children(line) if child != 'no other']:
            all_bags[child] = Bag(child)
    for line in data:
        parent = line.split(' bags')[0]
        # Text after the string 'contain ' is the CSV list of children
        # Don't take the last character; it's the EOL dot
        children = get_children(line)
        for child in children:
            if child == 'no other':
                break
            child_count = int(child.split(' ')[0])
            child_name = child.split(' ', 1)[1]
            all_bags[parent].add_child(all_bags[child_name], child_count)
    return all_bags


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
    bags = parse_bags(data)
    print(bags['shiny gold'].capacity())