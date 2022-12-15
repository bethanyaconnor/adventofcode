
def simulate_falling_sand(sand_map)
  resting_sand_count = 0
  while true
    sand_x = 500
    sand_y = 0

    return resting_sand_count unless sand_map[sand_y][sand_x] == '.'

    #sand_map.each {|row| puts row.inspect }
    while true
      return resting_sand_count if sand_y >= sand_map.length-1
      if sand_map[sand_y+1][sand_x] == '.'
        #puts "moving down"
        sand_y = sand_y + 1
      elsif sand_x > 0 && sand_map[sand_y+1][sand_x-1] == '.'
        #puts "moving left and down"
        sand_x = sand_x - 1
        sand_y = sand_y + 1
      elsif sand_x <= sand_map[0].length - 1 && sand_map[sand_y+1][sand_x+1] == '.'
        #puts "moving right and down"
        sand_x = sand_x + 1
        sand_y = sand_y + 1
      else
        resting_sand_count += 1
        #puts "resting at #{sand_x},#{sand_y}"
        sand_map[sand_y][sand_x] = 'o'
        break
      end
    end
  end
  return resting_sand_count
end



def part_1
  max_x = 0
  max_y = 0

  file_lines = File.readlines(ARGV[0])

  file_lines.each do |line|
    points = line.split(' -> ')
    points.each do |point|
      xy = point.split(',').map(&:to_i)
      max_x = xy[0] if xy[0] > max_x
      max_y = xy[1] if xy[1] > max_y
    end
  end

  sand_map = []
  (0..max_y).each do
    sand_map.append(Array.new(max_x+1) { '.' })
  end

  file_lines.each do |line|
    points = line.split(' -> ').map {|p| p.split(',').map(&:to_i) }
    (0...(points.length-1)).each do |idx|
      point1 = points[idx]
      point2 = points[idx + 1]

      if point1[0] == point2[0]
        x = point1[0]
        min_y = [point1[1], point2[1]].min
        max_y = [point1[1], point2[1]].max

        (min_y..max_y).each do |y|
          sand_map[y][x] = '#'
        end
      else
        y = point1[1]
        min_x = [point1[0], point2[0]].min
        max_x = [point1[0], point2[0]].max

        (min_x..max_x).each do |x|
          sand_map[y][x] = '#'
        end
      end
    end

  end

  puts "Part 1: #{simulate_falling_sand(sand_map)}"
end


def part_2
  max_x = 0
  max_y = 0

  file_lines = File.readlines(ARGV[0])

  file_lines.each do |line|
    points = line.split(' -> ')
    points.each do |point|
      xy = point.split(',').map(&:to_i)
      max_x = xy[0] if xy[0] > max_x
      max_y = xy[1] if xy[1] > max_y
    end
  end

  sand_map = []
  (0..(max_y+1)).each do
    sand_map.append(Array.new(max_x*2) { '.' })
  end
  sand_map.append(Array.new(max_x*2) { '#' })

  file_lines.each do |line|
    points = line.split(' -> ').map {|p| p.split(',').map(&:to_i) }
    (0...(points.length-1)).each do |idx|
      point1 = points[idx]
      point2 = points[idx + 1]

      if point1[0] == point2[0]
        x = point1[0]
        min_y = [point1[1], point2[1]].min
        max_y = [point1[1], point2[1]].max

        (min_y..max_y).each do |y|
          sand_map[y][x] = '#'
        end
      else
        y = point1[1]
        min_x = [point1[0], point2[0]].min
        max_x = [point1[0], point2[0]].max

        (min_x..max_x).each do |x|
          sand_map[y][x] = '#'
        end
      end
    end

  end

  puts "Part 2: #{simulate_falling_sand(sand_map)}"
end



#sand_map.each {|row| puts row.inspect }
part_1
part_2
