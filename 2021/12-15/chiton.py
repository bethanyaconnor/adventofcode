import sys

def shortest_path(grid):
    dist = []
    visited = []
    for i in range(len(grid)):
        dist.append([None]*len(grid[0]))
        visited.append([False]*len(grid[0]))
    dist[0][0] = 0
    num_visited = 1

    toVisit = [(0,0)]

    while num_visited < len(grid) * len(grid[0]):
        nodeRow = None
        nodeCol = None
        min_dist_left = None
        #for row in range(len(grid)):
        #    for col in range(len(grid[0])):
        #        if visited[row][col]:
        #            continue
        #        if dist[row][col] == None:
        #            continue
        #        if min_dist_left == None or dist[row][col] < min_dist_left:
        #            min_dist_left = dist[row][col]
        #            nodeRow = row
        #            nodeCol = col
        for possibleNode in toVisit:
            (row, col) = possibleNode
            if visited[row][col]:
                continue
            if dist[row][col] == None:
                continue
            if min_dist_left == None or dist[row][col] < min_dist_left:
                min_dist_left = dist[row][col]
                nodeRow = row
                nodeCol = col
        if nodeRow == len(grid) - 1 and nodeCol == len(grid[0]) - 1:
            return min_dist_left
        visited[nodeRow][nodeCol] = True
        toVisit.remove((nodeRow, nodeCol))
        nodeDist = min_dist_left
        if nodeRow > 0:
            if not visited[nodeRow - 1][nodeCol]:
                newDist = min_dist_left + grid[nodeRow - 1][nodeCol]
                if dist[nodeRow - 1][nodeCol] == None or newDist < dist[nodeRow - 1][nodeCol]:
                    wasNone = dist[nodeRow - 1][nodeCol] == None
                    if wasNone:
                        toVisit.append((nodeRow - 1, nodeCol))
                    dist[nodeRow - 1][nodeCol] = newDist
        if nodeRow < len(grid) - 1:
            if not visited[nodeRow + 1][nodeCol]:
                newDist = min_dist_left + grid[nodeRow + 1][nodeCol]
                if dist[nodeRow + 1][nodeCol] == None or newDist < dist[nodeRow + 1][nodeCol]:
                    wasNone = dist[nodeRow + 1][nodeCol] == None
                    if wasNone:
                        toVisit.append((nodeRow + 1, nodeCol))
                    dist[nodeRow + 1][nodeCol] = newDist
        if nodeCol > 0:
            if not visited[nodeRow][nodeCol - 1]:
                newDist = min_dist_left + grid[nodeRow][nodeCol - 1]
                if dist[nodeRow][nodeCol - 1] == None or newDist < dist[nodeRow][nodeCol - 1]:
                    wasNone = dist[nodeRow][nodeCol - 1] == None
                    if wasNone:
                        toVisit.append((nodeRow, nodeCol - 1))
                    dist[nodeRow][nodeCol - 1] = newDist
        if nodeCol < len(grid[0]) - 1:
            if not visited[nodeRow][nodeCol + 1]:
                newDist = min_dist_left + grid[nodeRow][nodeCol + 1]
                if dist[nodeRow][nodeCol + 1] == None or newDist < dist[nodeRow][nodeCol + 1]:
                    wasNone = dist[nodeRow][nodeCol + 1] == None
                    if wasNone:
                        toVisit.append((nodeRow, nodeCol + 1))
                    dist[nodeRow][nodeCol + 1] = newDist
    return None


def part_1(grid):
    return shortest_path(grid)

def part_2(grid):
    large_grid = []
    for row in grid:
        copiedRow = row.copy()
        newRow = row.copy()
        for i in range(4):
            for j in range(len(copiedRow)):
                copiedRow[j] += 1
                if copiedRow[j] > 9:
                    copiedRow[j] = 1
            newRow.extend(copiedRow.copy())
        large_grid.append(newRow)
    for i in range(4):
        for j in range(len(grid)):
            copiedRow = large_grid[i * len(grid) + j].copy()
            for k in range(len(copiedRow)):
                copiedRow[k] += 1
                if copiedRow[k] > 9:
                    copiedRow[k] = 1
            large_grid.append(copiedRow.copy())
    return shortest_path(large_grid)



f = open(sys.argv[1], 'r')
grid = []
for x in f:
    grid.append(list(map(lambda s : int(s), list(x.strip()))))

print("Part 1: " + str(part_1(grid)))
print("Part 2: " + str(part_2(grid)))
