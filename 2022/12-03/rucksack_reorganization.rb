def get_priority(char)
  if char.downcase == char
    char.ord - 96
  else
    char.ord - 64 + 26
  end
end

def part_1
  priority_sum = 0
  File.foreach(ARGV[0]) do |line|
    line = line.strip()
    compartment1_contents = line[0...(line.length/2)].split('').uniq
    compartment2_contents = line[(line.length/2)..-1].split('').uniq

    compartment1_contents.each do |char|
      if compartment2_contents.include?(char)
        priority_sum += get_priority(char)
      end
    end
  end

  puts "Part 1: #{priority_sum}"
end

def part_2
  priority_sum = 0
  file = File.open(ARGV[0])
  contents = file.readlines.map(&:chomp)
  start_index = 0

  while start_index < contents.length
    pack1 = contents[start_index].split('').uniq
    pack2 = contents[start_index+1].split('').uniq
    pack3 = contents[start_index+2].split('').uniq

    pack1.each do |char|
      priority_sum += get_priority(char) if pack2.include?(char) && pack3.include?(char)
    end

    start_index += 3
  end

  puts "Part 2: #{priority_sum}"
end

part_1
part_2
