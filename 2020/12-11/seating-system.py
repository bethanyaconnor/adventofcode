import copy

def is_occupied(grid, row, column):
    if row < 0 or column < 0:
        return False
    if row >= len(grid[0]) or column >= len(grid):
        return False
    return grid[column][row] == '#'

def apply_seating_rules_1(old_grid, new_grid):
    for column in range(0, len(old_grid)):
        for row in range(0, len(old_grid[0])):
            if old_grid[column][row] == '.':
                continue
            adjacent_occupied_seats = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if is_occupied(old_grid, row + i, column + j):
                        adjacent_occupied_seats += 1
            if adjacent_occupied_seats == 0:
                new_grid[column][row] = '#'
            elif adjacent_occupied_seats >= 4:
                new_grid[column][row] = 'L'
    return new_grid

def apply_seating_rules_2(old_grid, new_grid):
    for column in range(0, len(old_grid)):
        for row in range(0, len(old_grid[0])):
            if old_grid[column][row] == '.':
                continue
            viewable_occupied_seats = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    currentRow = row + i
                    currentColumn = column + j
                    while currentRow >= 0 and currentColumn >= 0 and currentRow < len(old_grid[0]) and currentColumn < len(old_grid) and old_grid[currentColumn][currentRow] == '.':
                        currentRow += i
                        currentColumn += j
                    if currentRow >= 0 and currentColumn >= 0 and currentRow < len(old_grid[0]) and currentColumn < len(old_grid) and old_grid[currentColumn][currentRow] == '#':
                        viewable_occupied_seats += 1

            if viewable_occupied_seats == 0:
                new_grid[column][row] = '#'
            elif viewable_occupied_seats >= 5:
                new_grid[column][row] = 'L'
    return new_grid

def grids_equal(grid1, grid2):
    if len(grid1) != len(grid2) or len(grid1[0]) != len(grid2[0]):
        return False
    for column in range(0, len(grid1)):
        for row in range(0, len(grid1[0])):
            if grid1[column][row] != grid2[column][row]:
                return False
    return True

def simulate_seating_1(grid):
    while True:
        new_grid = apply_seating_rules_1(grid, copy.deepcopy(grid))
        if grids_equal(grid, new_grid):
            return grid
        grid = copy.deepcopy(new_grid)

def simulate_seating_2(grid):
    while True:
        new_grid = apply_seating_rules_2(grid, copy.deepcopy(grid))
        if grids_equal(grid, new_grid):
            return grid
        grid = copy.deepcopy(new_grid)

def count_occupied_seats(grid):
    occupied_seats = 0
    for column in range(0, len(grid)):
        for row in range(0, len(grid[0])):
            if grid[column][row] == '#':
                occupied_seats += 1
    return occupied_seats

f = open("input.txt", "r")
grid = []
for x in f:
    grid.append(list(x.strip()))
steady_state_1 = simulate_seating_1(copy.deepcopy(grid))
occupied_seats_1 = count_occupied_seats(steady_state_1)
print("Part 1 answer: {}".format(occupied_seats_1))
steady_state_2 = simulate_seating_2(copy.deepcopy(grid))
occupied_seats_2 = count_occupied_seats(steady_state_2)
print("Part 2 answer: {}".format(occupied_seats_2))
