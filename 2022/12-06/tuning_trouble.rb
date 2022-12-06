
def find_marker(datastream, num_distinct)
  idx = num_distinct
  while idx < datastream.length
    if datastream[(idx-num_distinct)...idx].strip.split('').uniq.length == num_distinct
      return idx
    end
    idx += 1
  end
end

def part_1(datastream)
end

datastream = ARGF.read
puts "Part 1: #{find_marker(datastream, 4)}"
puts "Part 2: #{find_marker(datastream, 14)}"
