#!/usr/bin/env python3

import os
import sys
import itertools
import numpy


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Cube:
    def __init__(self, char):
        self.char = char
        # '.' for inactive, '#' for active
        if char == '.':
            self.active = False
        else:
            self.active = True

    def __str__(self):
        return self.char

    def copy(self):
        return Cube(self.char)


class Space:
    def __init__(self, data, dimensions):
        # Pretty sure this is going to be needed in part 2, but it gets overwritten for now
        self.space = self.create_dimensions(dimensions)
        self.dimensions = dimensions
        self.SLOPES = self.__get_slopes()
        plane = []
        for row in data:
            line = [Cube(char) for char in row]
            plane.append(line)
        self.space = [plane]

    def create_dimensions(self, dimensions, size=None):
        if dimensions == 1:
            return [Cube('.')]
        else:
            return [self.create_dimensions(dimensions - 1)]

    def get_cube(self, coords):
        coords = list(reversed(coords))
        try:
            return self.__get_cube_at(coords, self.space)
        except IndexError:
            return Cube('.')

    # Space is always expanding in a simulation
    def expand_space(self):
        new_space = []
        for plane in self.space:
            new_plane = []
            for line in plane:
                new_line = line[:]
                line.insert(0, Cube('.'))
                line.append(Cube('.'))
                new_plane.append(new_line)
            new_space.append(new_plane)
        self.space = new_space

        # Narrowed down to the last three dimensions, copy the existing space with a border of inactive cubes
        # if not isinstance(space[0][0][0], list):

        # if not isinstance(space[0], list):
        #     new_line = space[:]
        #     new_line.insert(0, Cube('.'))
        #     new_line.append(Cube('.'))
        #     return new_line
        # else:
        #     plane = expand(space[0])
        #     empty_plane = self.create_dimensions(self.dim)
        #     new_space = []
        #     for i in range(len(plane) + 2):
        #         new_space.append(plane)
        #     return new_space

    def get_space_size(self, space):
        if not isinstance(space[0], list):
            return [len(space)]
        else:
            return list(itertools.chain([len(space)], self.get_space_size(space[0])))

    def count_neighbors(self, coords):
        count = 0
        for slope in self.SLOPES:
            new_coords = numpy.add(coords, slope)
            if self.get_cube(new_coords).active:
                count += 1
        return count

    def simulate_reality(self, ticks):
        for i in range(ticks):
            # Make sure cubes have room to expand out if necessary
            self.expand_space()
            space_sizes = self.get_space_size(self.space)
            new_space = []
            ranges = [list(range(dim_size)) for dim_size in space_sizes]
            print(ranges)
            all_coords = list(itertools.product(*ranges))
            print(all_coords)
            for coords in all_coords:
                neighbor_count = self.count_neighbors(coords)
                cube = self.get_cube(coords)
                new_cube = cube.copy()
                if cube.active and neighbor_count not in (2, 3):
                    new_cube = Cube('.')
                elif not cube.active and neighbor_count == 3:
                    new_cube = Cube('#')

    def __get_cube_at(self, coords, space):
        # print(coords)
        # Want to return space[z][y][x], but for an arbitrary number of dimensions potentially
        if len(coords) == 1:
            return space[coords[0]]
        else:
            return self.__get_cube_at(coords[1:], space[coords[0]])

    def __get_slopes(self):
        seed = []
        for i in range(self.dimensions):
            # We want (N - 1) 0's, N 1's, and N -1's for the permutations to work correctly
            # This is because we never want to check our own coordinates of (0,0,0)
            if i != self.dimensions - 1:
                seed.append(0)
            seed.append(1)
            seed.append(-1)
        return set(itertools.permutations(seed, 3))

    def __str__(self):
        string = ''
        # Writing this strictly for 3 dimensions because it's just for my own debugging use
        for z, plane in enumerate(self.space):
            string += 'z: ' + str(z) + '\n'
            for line in plane:
                for cube in line:
                    string += str(cube)
                string += '\n'
        return string


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

    space = Space(data, 3)
    print(space)
    space.simulate_reality(1)
    print(space)
