import sys

def draw_lines(lines, width, height):
    grid = [([None]*width) for _ in range(height)]
    for x in range(width):
        for y in range(height):
            grid[y][x] = 0
    for line in lines:
        [x1, y1] = line[0]
        [x2, y2] = line[1]
        x_diff = abs(x1-x2)
        y_diff = abs(y1-y2)
        if y_diff > x_diff:
            step = 1 if y1 < y2 else -1
            x_step = (x2 - x1) / (y2 - y1)
            for y in range(y1, y2+step, step):
                x = round(x1 + x_step * (y - y1))
                print(x,y)
                grid[y][x] += 1
        else:
            step = 1 if x1 < x2 else -1
            y_step = (y2 - y1) / (x2 - x1)
            for x in range(x1, x2+step, step):
                y = round(y1 + y_step * (x - x1))
                grid[y][x] += 1
    return grid

def find_danger_aread(lines, width, height):
    grid = draw_lines(lines, width, height)
    danger_areas = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] >= 2:
                danger_areas += 1
    print("Part 1: " + str(danger_areas))

f = open(sys.argv[1], "r")
lines = []
max_x = 0
max_y = 0
for x in f:
    pairs = x.strip().split(' -> ')
    pairs[0] = pairs[0].split(',')
    pairs[0] = list(map(lambda s: int(s), pairs[0]))
    pairs[1] = pairs[1].split(',')
    pairs[1] = list(map(lambda s: int(s), pairs[1]))
    max_x = max(max_x, pairs[0][0], pairs[1][0])
    max_y = max(max_y, pairs[0][1], pairs[1][1])
    lines.append(pairs)

find_danger_areas(lines, max_x+1, max_y+1)


