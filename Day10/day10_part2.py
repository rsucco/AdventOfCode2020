#!/usr/bin/env python3

import os
import sys


class Adapter:
    def __init__(self, output):
        self.output = output
        self.input = list(range(max(output - 3, 0), output))
        self.connections = []
        self.path_cache = {}

    def accepts(self, other):
        if other.output in self.input:
            return True
        else:
            return False

    # This is where the magic happens
    # Brute forcing this is easy to write but takes forever, so some shortcuts are necessary
    def count_paths(self):
        # This adapter is basically irrelevant
        if len(self.connections) == 0:
            return 1
        # Ugh I have to calculate something
        else:
            total_connections = 0
            for connection in self.connections:
                # Check if it's in the cache, a miss will make me get all recursive up in here
                if connection not in self.path_cache.keys():
                    # Calculate path lengths for this connection recursively and save to the cache
                    self.path_cache[connection] = connection.count_paths()
                # The value will either be in the cache from earlier or will be freshly calculated
                total_connections += self.path_cache[connection]
            return total_connections

def get_adapters(data):
    adapters = list(sorted(int(datum) for datum in data))
    # The wall starts at 0 jolts
    adapters.insert(0,0)
    # The device's built-in adapter is always 3 higher than the highest
    adapters.append(max(adapters) + 3)
    return adapters

def get_permutations(data):
    adapters = [Adapter(adapter) for adapter in get_adapters(data)]
    # Add all of the other adapters that an adapter can connect to
    for adapter in adapters:
        # I feel guilty for not writing a comment here but the next line is basically plain English, google it
        adapter.connections = [other_adapter for other_adapter in adapters if other_adapter.accepts(adapter)]
    # Count the number of paths from the first adapter to the ending 
    return adapters[0].count_paths()

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
    
    print(get_permutations(data))
