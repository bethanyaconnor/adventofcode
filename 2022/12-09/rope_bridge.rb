
def touching?(h_x_pos, h_y_pos, t_x_pos, t_y_pos)
  return true if (h_x_pos - t_x_pos).abs <= 1 && (h_y_pos - t_y_pos).abs <= 1
  false
end

def calculate_t_position(h_x_pos, h_y_pos, t_x_pos, t_y_pos)
 return [t_x_pos, t_y_pos] if touching?(h_x_pos, h_y_pos, t_x_pos, t_y_pos)

  if h_x_pos == t_x_pos
    return [t_x_pos, t_y_pos + 1] if h_y_pos > t_y_pos
    return [t_x_pos, t_y_pos - 1]
  elsif h_y_pos == t_y_pos
    return [t_x_pos + 1, t_y_pos] if h_x_pos > t_x_pos
    return [t_x_pos - 1, t_y_pos]
  else
    if h_x_pos > t_x_pos
      if h_y_pos > t_y_pos
        return [t_x_pos + 1, t_y_pos + 1]
      else
        return [t_x_pos + 1, t_y_pos - 1]
      end
    else
      if h_y_pos > t_y_pos
        return [t_x_pos - 1, t_y_pos + 1]
      else
        return [t_x_pos - 1, t_y_pos - 1]
      end
    end
  end
end

def part_1
  h_x_pos = 0
  h_y_pos = 0
  t_x_pos = 0
  t_y_pos = 0
  t_pos_list = ["0,0"]
  File.readlines(ARGV[0]).each do |line|
    split_line = line.strip.split(' ')
    dir = split_line[0]
    steps = split_line[1].to_i

    (0...steps).each do
      if dir == 'R'
        h_x_pos += 1
      elsif dir == 'L'
        h_x_pos -= 1
      elsif dir == 'U'
        h_y_pos += 1
      elsif dir == 'D'
        h_y_pos -= 1
      end

      new_t_pos = calculate_t_position(h_x_pos, h_y_pos, t_x_pos, t_y_pos)

      t_x_pos = new_t_pos[0]
      t_y_pos = new_t_pos[1]

      t_pos_list.append("#{t_x_pos},#{t_y_pos}")

    end
  end
  puts "Part 1: #{t_pos_list.uniq.length}"
end

def part_2
  h_x_pos = 0
  h_y_pos = 0
  tail_positions = (0...9).map {|i| [0,0] }
  final_t_pos_list = ["0,0"]
  File.readlines(ARGV[0]).each do |line|
    split_line = line.strip.split(' ')
    dir = split_line[0]
    steps = split_line[1].to_i

    (0...steps).each do
      if dir == 'R'
        h_x_pos += 1
      elsif dir == 'L'
        h_x_pos -= 1
      elsif dir == 'U'
        h_y_pos += 1
      elsif dir == 'D'
        h_y_pos -= 1
      end

      tail_positions[0] = calculate_t_position(h_x_pos, h_y_pos, tail_positions[0][0], tail_positions[0][1])

      (1...9).each do |i|
        tail_positions[i] = calculate_t_position(tail_positions[i-1][0], tail_positions[i-1][1], tail_positions[i][0], tail_positions[i][1])
      end


      final_t_pos_list.append("#{tail_positions[-1][0]},#{tail_positions[-1][1]}")

    end
  end
  puts "Part 2: #{final_t_pos_list.uniq.length}"
end

part_1
part_2

