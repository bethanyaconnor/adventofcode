

def part_1
  notable_cycles = [20, 60, 100, 140, 180, 220]
  current_signal_strength = 1
  current_cycle = 1
  output = 0
  File.readlines(ARGV[0]).each do |line|
    line.strip!
    if line == 'noop'
      if notable_cycles.include?(current_cycle)
        output += current_signal_strength * current_cycle
      end
      current_cycle += 1
    else
      (0...2).each do
        if notable_cycles.include?(current_cycle)
          output += current_signal_strength * current_cycle
        end
        current_cycle += 1
      end
      current_signal_strength += line.split(' ')[1].to_i
    end
  end

  puts "Part 1: #{output}"
end

def calculate_crt(current_cycle, current_signal_strength)
  return '#' if ((current_cycle%20)-current_signal_strength).abs <= 1
  return '.'
end

def part_2
  notable_cycles = [40, 80, 120, 160, 200, 240]
  current_signal_strength = 1
  current_cycle = 1
  current_row = ""
  puts "Part 2:"
  File.readlines(ARGV[0]).each do |line|
    line.strip!
    if line == 'noop'
      if notable_cycles.include?(current_row.length)
        puts current_row
        current_row = ""
      end
      if (current_row.length-current_signal_strength).abs <= 1
        current_row += '#'
      else
        current_row += '.'
      end
      current_cycle += 1
    else
      (0...2).each do
        if notable_cycles.include?(current_row.length)
          puts current_row
          current_row = ""
        end
        if (current_row.length-current_signal_strength).abs <= 1
          current_row += '#'
        else
          current_row += '.'
        end
        current_cycle += 1
      end
      current_signal_strength += line.split(' ')[1].to_i
    end
  end
  puts current_row
end

part_1
part_2
