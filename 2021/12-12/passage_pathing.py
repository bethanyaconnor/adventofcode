import sys

def breath_first_search_count_1(edge_map, visited_map, current_node):
    if current_node == 'end':
        return 1
    count = 0
    copied_visited_map = visited_map.copy()
    copied_visited_map[current_node] = True
    for node in edge_map[current_node]:
        if node == 'start':
            continue
        if copied_visited_map[node] and node.islower():
            continue
        count += breath_first_search_count_1(edge_map, copied_visited_map, node)
    return count

def breath_first_search_count_2(edge_map, visited_map, current_node, path):
    if current_node == 'end':
        return 1
    count = 0
    copied_visited_map = visited_map.copy()
    if current_node.islower():
        copied_visited_map[current_node] += 1
    for node in edge_map[current_node]:
        if node == 'start':
            continue
        if node.islower() and copied_visited_map[node] > 0 and 2 in copied_visited_map.values():
            continue
        count += breath_first_search_count_2(edge_map, copied_visited_map, node, path + ',' + node)
    return count



def part_1(edge_map):
    visited_map = {}
    for key in edge_map.keys():
        visited_map[key] = False
    return breath_first_search_count_1(edge_map, visited_map, 'start')

def part_2(edge_map):
    visited_map = {}
    for key in edge_map.keys():
        visited_map[key] = 0
    return breath_first_search_count_2(edge_map, visited_map, 'start', 'start')



f = open(sys.argv[1], 'r')
edge_map = {}
for x in f:
    nodes = x.strip().split('-')
    if edge_map.get(nodes[0]):
        edge_map.get(nodes[0]).append(nodes[1])
    else:
        edge_map[nodes[0]] = [nodes[1]]
    if edge_map.get(nodes[1]):
        edge_map.get(nodes[1]).append(nodes[0])
    else:
        edge_map[nodes[1]] = [nodes[0]]

print("Part 1: " + str(part_1(edge_map)))
print("Part 2: " + str(part_2(edge_map)))
