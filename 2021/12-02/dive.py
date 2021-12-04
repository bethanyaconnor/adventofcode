
import sys

def find_actual_position(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        [direction, amount] = command.split()
        if direction == 'forward':
            horizontal_position += int(amount)
            depth += aim * int(amount)
        elif direction == 'up':
            aim -= int(amount)
        elif direction == 'down':
            aim += int(amount)
        else:
            print("Dont know what to do with " + command)
    return horizontal_position * depth

def find_position(commands):
    horizontal_position = 0
    depth = 0
    for command in commands:
        words = command.split()
        if words[0] == 'forward':
            horizontal_position += int(words[1])
        elif words[0] == 'up':
            depth -= int(words[1])
        elif words[0] == 'down':
            depth += int(words[1])
        else:
            print("Dont know what to do with " + command)
    return horizontal_position * depth


f = open(sys.argv[1], "r")
commands = []
for x in f:
    commands.append(x)

print("Part 1: " + str(find_position(commands)))
print("Part 2: " + str(find_actual_position(commands)))
