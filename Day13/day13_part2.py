#!/usr/bin/env python3

import os
import sys


def get_departure_time(bus_data, earliest_departure):
    bus_ids = [int(bus) for bus in bus_data.split(',') if bus != 'x']
    schedule = {}
    for bus_id in bus_ids:
        bus_time = bus_id
        while bus_time < earliest_departure:
            bus_time += bus_id
        schedule[bus_id] = bus_time
    earliest_bus_time = min(schedule.values())
    earliest_bus_id = min(schedule, key=schedule.get)
    print('earliest departure time:', earliest_departure)
    print('earliest bus from each route:', schedule)
    print('earliest bus id:', earliest_bus_id,
          'departure time:', earliest_bus_time)
    print('answer:', earliest_bus_id * (earliest_bus_time - earliest_departure))


def get_gold_coin(bus_data):
    bus_offsets = {int(bus_id): i for i, bus_id in enumerate(
        bus_data.split(',')) if bus_id != 'x'}
    print(bus_offsets)
    increment = list(bus_offsets.keys())[0]
    t = 0

    while True:
        t += increment
        if t % mod:
            result = t + increment
            print(result)
            break


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
    earliest_departure = int(data[0])
    bus_data = data[1]
    get_gold_coin(bus_data)
