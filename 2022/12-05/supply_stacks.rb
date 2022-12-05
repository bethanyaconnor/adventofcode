
def part_1
  file = File.open(ARGV[0])
  lines = file.readlines.map(&:chomp)

  break_index = lines.find_index {|l| l.strip.empty? }

  instructions = lines[(break_index+1)..-1]

  num_columns = lines[break_index-1].strip[-1].to_i
  columns = []
  (1..num_columns).to_a.each do |c|
    lines[0...(break_index-1)].each do |line|
      index = 4 * c - 3
      columns[c] ||= []
      columns[c].unshift(line[index]) unless line[index].strip.empty?
    end
  end

  instructions.each do |instruction|
    split_instruction = instruction.strip.split(' ')
    num_to_move = split_instruction[1].to_i
    origin_stack = split_instruction[3].to_i
    destination_stack = split_instruction[5].to_i
    (0...num_to_move).to_a.each do
      crate = columns[origin_stack].pop
      columns[destination_stack].push(crate)
    end
  end

  output = ""
  (1..num_columns).to_a.each do |c|
    output += columns[c][-1]
  end

  puts "Part 1: #{output}"
end

def part_2
  file = File.open(ARGV[0])
  lines = file.readlines.map(&:chomp)

  break_index = lines.find_index {|l| l.strip.empty? }

  instructions = lines[(break_index+1)..-1]

  num_columns = lines[break_index-1].strip[-1].to_i
  columns = []
  (1..num_columns).to_a.each do |c|
    lines[0...(break_index-1)].each do |line|
      index = 4 * c - 3
      columns[c] ||= []
      columns[c].unshift(line[index]) unless line[index].strip.empty?
    end
  end

  instructions.each do |instruction|
    split_instruction = instruction.strip.split(' ')
    num_to_move = split_instruction[1].to_i
    origin_stack_index = split_instruction[3].to_i
    origin_stack = columns[origin_stack_index]
    destination_stack = columns[split_instruction[5].to_i]

    low_index = origin_stack.length - num_to_move
    stack_to_move = origin_stack[low_index..-1]
    columns[origin_stack_index] = origin_stack[0...low_index]
    destination_stack.concat(stack_to_move)
  end

  output = ""
  (1..num_columns).to_a.each do |c|
    output += columns[c][-1]
  end

  puts "Part 2: #{output}"
end

part_1
part_2
