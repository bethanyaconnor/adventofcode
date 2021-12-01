def find_trees_hit(forest_map, run, rise):
  currentX = run
  currentY = rise
  trees_hit = 0
  while currentY < len(forest_map):
      if forest_map[currentY][currentX % len(forest_map[0])] == '#':
          trees_hit += 1
      currentX += run
      currentY += rise
  return trees_hit

f = open("input.txt", "r")
forest_map = []
for x in f:
  forest_map.append(list(x.strip()))
running_product = 1
running_product *= find_trees_hit(forest_map, 1, 1)
running_product *= find_trees_hit(forest_map, 3, 1)
running_product *= find_trees_hit(forest_map, 5, 1)
running_product *= find_trees_hit(forest_map, 7, 1)
running_product *= find_trees_hit(forest_map, 1, 2)
print(running_product)
