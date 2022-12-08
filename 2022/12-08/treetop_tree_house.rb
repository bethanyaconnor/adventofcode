
def calculate_scenic_score(tree_grid, x, y)
  return 0 if x == 0 || y == 0 || x == (tree_grid[0].length-1) || y == (tree_grid.length-1)

  current_height = tree_grid[y][x]

  left_score = 0
  (x-1).downto(0).each do |x1|
    left_score +=1
    break if tree_grid[y][x1] >= current_height
  end

  up_score = 0
  (y-1).downto(0).each do |y1|
    up_score += 1
    break if tree_grid[y1][x] >= current_height
  end

  right_score = 0
  ((x+1)...tree_grid[0].length).each do |x1|
    right_score += 1
    break if tree_grid[y][x1] >= current_height
  end

  down_score = 0
  ((y+1)...tree_grid.length).each do |y1|
    down_score += 1
    break if tree_grid[y1][x] >= current_height
  end

  left_score * up_score * right_score * down_score
end

def is_visible?(tree_grid, x, y)
  return true if x == 0 || y == 0 || x == (tree_grid[0].length-1) || y == (tree_grid.length-1)

  current_height = tree_grid[y][x]
  return true unless (0..(x-1)).any?{|x1| tree_grid[y][x1] >= current_height}
  return true unless (0..(y-1)).any?{|y1| tree_grid[y1][x] >= current_height}
  return true unless ((x+1)...tree_grid[0].length).any? {|x1| tree_grid[y][x1] >= current_height}
  return true unless ((y+1)...tree_grid.length).any? {|y1| tree_grid[y1][x] >= current_height}

  return false
end

def part_1(tree_grid)
  visible_trees = 0
  (0...tree_grid[0].length).each do |x|
    (0...tree_grid.length).each do |y|
      visible_trees += 1 if is_visible?(tree_grid, x, y)
    end
  end
  puts "Part 1: #{visible_trees}"
end

def part_2(tree_grid)
  max_scenic_score = 0
  (0...tree_grid[0].length).each do |x|
    (0...tree_grid.length).each do |y|
      scenic_score = calculate_scenic_score(tree_grid, x, y)
      max_scenic_score = scenic_score if scenic_score > max_scenic_score
    end
  end
  puts "Part 2: #{max_scenic_score}"
end

tree_grid = []
File.readlines(ARGV[0]).each do |line|
  tree_grid.append(line.strip.split('').map(&:to_i))
end

part_1(tree_grid)
part_2(tree_grid)
