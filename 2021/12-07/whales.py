import sys
import math

def part_1(starting_positions):
    starting_positions.sort()
    median = starting_positions[round(len(starting_positions) / 2)]
    fuel = 0
    for position in starting_positions:
        fuel += abs(position - median)
    return fuel

def part_2(starting_positions):
    starting_positions.sort()
    average = (sum(starting_positions) / len(starting_positions))
    ceil_fuel = 0
    floor_fuel = 0
    for position in starting_positions:
        step = abs(position - math.ceil(average))
        ceil_fuel += round((step * (step + 1)) / 2)
        step = abs(position - math.floor(average))
        floor_fuel += round((step * (step + 1)) / 2)
    return min(ceil_fuel, floor_fuel)



f = open(sys.argv[1], 'r')
starting_positions = f.read().strip().split(',')
starting_positions = list(map(lambda s : int(s), starting_positions))
print("Part 1: " + str(part_1(starting_positions)))
print("Part 2: " + str(part_2(starting_positions)))

