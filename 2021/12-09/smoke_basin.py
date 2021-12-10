import sys

def find_low_points(cavemap):
    low_points = []
    for row in range(len(cavemap)):
        for col in range(len(cavemap[0])):
            current_height = cavemap[row][col]
            if col > 0 and cavemap[row][col-1] <= current_height:
                continue
            if row > 0 and cavemap[row-1][col] <= current_height:
                continue
            if row + 1 < len(cavemap) and cavemap[row+1][col] <= current_height:
                continue
            if col + 1 < len(cavemap[0]) and cavemap[row][col+1] <= current_height:
                continue
            low_points.append((row, col, current_height)) 
    return low_points

def part_1(cavemap):
    low_points = find_low_points(cavemap)
    risk_sum = 0
    for point in low_points:
        risk_sum += point[2] + 1
    return risk_sum

def find_basin(cavemap, visited, row, col):
    current_height = cavemap[row][col]
    if current_height == 9:
        return 0
    if visited[row][col]:
        return 0
    size = 1
    visited[row][col] = True
    if col > 0 and cavemap[row][col-1] >= current_height:
        size += find_basin(cavemap, visited, row, col - 1)
    if row > 0 and cavemap[row-1][col] >= current_height:
        size += find_basin(cavemap, visited, row - 1, col)
    if row + 1 < len(cavemap) and cavemap[row+1][col] >= current_height:
        size += find_basin(cavemap, visited, row + 1, col)
    if col + 1 < len(cavemap[0]) and cavemap[row][col+1] >= current_height:
        size += find_basin(cavemap, visited, row, col + 1)
    return size


def part_2(cavemap):
    visited = []
    for i in range(len(cavemap)):
        visited.append([False]*len(cavemap[0]))
    low_points = find_low_points(cavemap)
    basin_sizes = []
    for point in low_points:
        basin_sizes.append(find_basin(cavemap, visited, point[0], point[1]))
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

f = open(sys.argv[1], 'r')
cavemap = []
for x in f:
    cavemap.append(list(map(lambda s : int(s), list(x.strip()))))

print("Part 1: " + str(part_1(cavemap)))
print("Part 2: " + str(part_2(cavemap)))
