
def find_coordinate(heightmap, symbol)
  heightmap.each_with_index do |row, row_idx|
    row.each_with_index do |mark, col_idx|
      return [row_idx, col_idx] if mark == symbol
    end
  end
end

def find_next_coordinate(node_map)
  min = Float::INFINITY
  min_loc = nil
  node_map.each_with_index do |row, row_idx|
    row.each_with_index do |node, col_idx|
      if !node[:visited] && node[:distance] < min
        min = node[:distance]
        min_loc = [row_idx, col_idx]
      end
    end
  end
  return min_loc
end

def find_shortest_path(heightmap, starting_coordinate, ending_coordinate)
  node_map = Array.new(heightmap.length){Array.new(heightmap[0].length){Hash.new}}
  node_map.each do |row|
    row.each do |node|
      node[:visited] = false
      node[:distance] = Float::INFINITY
    end
  end
  node_map[starting_coordinate[0]][starting_coordinate[1]][:distance] = 0
  current_coordinate = find_next_coordinate(node_map)
  while current_coordinate != ending_coordinate
    row_idx = current_coordinate[0]
    col_idx = current_coordinate[1]
    height_value = heightmap[row_idx][col_idx]
    height_value = 'a' if height_value == 'S'
    height_value = 'z' if height_value == 'E'
    node = node_map[row_idx][col_idx]

    if row_idx > 0
      neighbor_value = heightmap[row_idx-1][col_idx]
      neighbor_value = 'z' if neighbor_value == 'E'
      neighbor_node = node_map[row_idx-1][col_idx]
      if !neighbor_node[:visited] && neighbor_value.ord <= height_value.ord + 1
        new_distance = node[:distance] + 1
        neighbor_node[:distance] = new_distance if new_distance < neighbor_node[:distance]
      end
    end

    if col_idx > 0
      neighbor_value = heightmap[row_idx][col_idx-1]
      neighbor_value = 'z' if neighbor_value == 'E'
      neighbor_node = node_map[row_idx][col_idx-1]
      if !neighbor_node[:visited] && neighbor_value.ord <= height_value.ord + 1
        new_distance = node[:distance] + 1
        neighbor_node[:distance] = new_distance if new_distance < neighbor_node[:distance]
      end
    end

    if row_idx < heightmap.length - 1
      neighbor_value = heightmap[row_idx+1][col_idx]
      neighbor_value = 'z' if neighbor_value == 'E'
      neighbor_node = node_map[row_idx+1][col_idx]
      if !neighbor_node[:visited] && neighbor_value.ord <= height_value.ord + 1
        new_distance = node[:distance] + 1
        neighbor_node[:distance] = new_distance if new_distance < neighbor_node[:distance]
      end
    end

    if col_idx < heightmap[0].length - 1
      neighbor_value = heightmap[row_idx][col_idx+1]
      neighbor_value = 'z' if neighbor_value == 'E'
      neighbor_node = node_map[row_idx][col_idx+1]
      if !neighbor_node[:visited] && neighbor_value.ord <= height_value.ord + 1
        new_distance = node[:distance] + 1
        neighbor_node[:distance] = new_distance if new_distance < neighbor_node[:distance]
      end
    end
    node[:visited] = true
    current_coordinate = find_next_coordinate(node_map)
    return Float::INFINITY if current_coordinate.nil?
  end
  return node_map[ending_coordinate[0]][ending_coordinate[1]][:distance]
end

def part_1(heightmap)
  starting_coordinate = find_coordinate(heightmap, 'S')
  ending_coordinate = find_coordinate(heightmap, 'E')
  puts "Part 1: #{find_shortest_path(heightmap, starting_coordinate, ending_coordinate)}"
end

def part_2(heightmap)
  ending_coordinate = find_coordinate(heightmap, 'E')
  possible_starting_coordinates = []
  heightmap.each_with_index do |row, row_idx|
    row.each_with_index do |mark, col_idx|
      possible_starting_coordinates.append([row_idx, col_idx]) if mark == 'S' || mark == 'a'
    end
  end
  min_dist = Float::INFINITY
  possible_starting_coordinates.each do |starting_coordinate|
    dist = find_shortest_path(heightmap, starting_coordinate, ending_coordinate)
    min_dist = dist if dist < min_dist
  end
  puts "Part 2: #{min_dist}"
end

heightmap = []
File.readlines(ARGV[0]).each do |line|
  heightmap.append(line.strip.split(''))
end
part_1(heightmap)
part_2(heightmap)
