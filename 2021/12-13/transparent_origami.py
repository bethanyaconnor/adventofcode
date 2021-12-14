import sys

def part_1(dots, instructions, max_x, max_y):
    grid = []
    for i in range(max_y+1):
        grid.append(['.']*(max_x+1))
    for [x, y] in dots:
        grid[y][x] = '#'

    instructions = instructions[0:1]
    for instruction in instructions:
        new_grid = []
        if instruction[0] == 'x':
            for y in range(len(grid)):
                row = grid[y].copy()
                for x in range(1, instruction[1]+1):
                    if row[instruction[1] + x] == '#':
                            row[instruction[1] - x] = '#'
                row = row[0:instruction[1]]
                new_grid.append(row)
        else:
            for y_diff in range(instruction[1], 1, -1):
                early_row = grid[instruction[1] - y_diff].copy()
                late_row = grid[instruction[1] + y_diff].copy()
                for x in range(len(late_row)):
                    if late_row[x] == '#':
                        early_row[x] = '#'
                new_grid.append(early_row)
        grid = new_grid
    dot_count = 0
    for y in range(len(new_grid)):
        for x in range(len(new_grid[0])):
            if new_grid[y][x] == '#':
                dot_count += 1
    return dot_count


def part_2(dots, instructions, max_x, max_y):
    grid = []
    for i in range(max_y+1):
        grid.append([' ']*(max_x+1))
    for [x, y] in dots:
        grid[y][x] = '#'

    for instruction in instructions:
        new_grid = []
        if instruction[0] == 'x':
            for y in range(len(grid)):
                row = grid[y].copy()
                for x in range(instruction[1]):
                    if row[len(row)-1-x] == '#':
                            row[x] = '#'
                row = row[0:instruction[1]]
                new_grid.append(row)
        else:
            for y in range(instruction[1]):
                early_row = grid[y].copy()
                late_row = grid[len(grid)-y-1].copy()
                for x in range(len(late_row)):
                    if late_row[x] == '#':
                        early_row[x] = '#'
                new_grid.append(early_row)
        grid = new_grid
    for y in range(len(new_grid)):
        print(''.join(grid[y]))


f = open(sys.argv[1], 'r')
dots = []
max_x = 0
max_y = 0
instructions = []
for x in f:
    if len(x.strip()) == 0:
        continue
    elif x.startswith('fold'):
        fold_line = x.strip().split()[-1].split('=')
        instructions.append((fold_line[0], int(fold_line[1])))
    else:
        coordinates = list(map(lambda s : int(s), x.strip().split(',')))
        if coordinates[0] > max_x:
            max_x = coordinates[0]
        if coordinates[1] > max_y:
            max_y = coordinates[1]
        dots.append(coordinates)

if max_x % 2 == 1:
    max_x += 1
if max_y % 2 == 1:
    max_y += 1
print("Part 1: " + str(part_1(dots, instructions, max_x, max_y)))
print("Part 2: ")
part_2(dots, instructions, max_x, max_y)
