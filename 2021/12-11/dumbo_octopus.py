import sys

def increase_energies(grid):
    for row in range(10):
        for col in range(10):
            grid[row][col] += 1

def handle_flash(grid, flashed, row, col):
    if grid[row][col] <= 9:
        return
    if flashed[row][col]:
        return
    flashed[row][col] = True
    if row > 0:
        grid[row - 1][col] += 1
        handle_flash(grid, flashed, row - 1, col)
        if col > 0:
            grid[row - 1][col-1] += 1
            handle_flash(grid, flashed, row - 1, col - 1)
        if col < 9:
            grid[row - 1][col+1] += 1
            handle_flash(grid, flashed, row - 1, col + 1)
    if row < 9:
        grid[row + 1][col] += 1
        handle_flash(grid, flashed, row + 1, col)
        if col > 0:
            grid[row + 1][col-1] += 1
            handle_flash(grid, flashed, row + 1, col - 1)
        if col < 9:
            grid[row + 1][col+1] += 1
            handle_flash(grid, flashed, row + 1, col + 1)
    if col > 0:
        grid[row][col - 1] += 1
        handle_flash(grid, flashed, row, col - 1)
    if col < 9:
        grid[row][col + 1] += 1
        handle_flash(grid, flashed, row, col + 1)


def percolate_flashes(grid):
    already_flashed = []
    for i in range(10):
        already_flashed.append([False]*10)
    for row in range(10):
        for col in range(10):
            if grid[row][col] > 9:
                handle_flash(grid, already_flashed, row, col)
    for row in range(10):
        for col in range(10):
            if not already_flashed[row][col]:
                return False
    return True

def count_and_reset_flashes(grid):
    count = 0
    for row in range(10):
        for col in range(10):
            if grid[row][col] > 9:
                count += 1
                grid[row][col] = 0
    return count

def part_1(starting_grid):
    grid = starting_grid
    count = 0
    for i in range(100):
        increase_energies(grid)
        percolate_flashes(grid)
        count += count_and_reset_flashes(grid)
    return count

def part_2(starting_grid):
    grid = starting_grid
    syncronized = False
    step = 0
    while not syncronized:
        step += 1
        increase_energies(grid)
        syncronized = percolate_flashes(grid)
        count_and_reset_flashes(grid)
    return step


f = open(sys.argv[1], 'r')
starting_grid_1 = []
starting_grid_2 = []
for x in f:
    starting_grid_1.append(list(map(lambda s : int(s), list(x.strip()))))
    starting_grid_2.append(list(map(lambda s : int(s), list(x.strip()))))
print("Part 1: " + str(part_1(starting_grid_1)))
print("Part 2: " + str(part_2(starting_grid_2)))
