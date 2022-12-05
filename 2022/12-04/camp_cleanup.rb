
def get_sections(start_num, end_num)
  (start_num..end_num).map(&:to_s)
end

def parse_sections(str)
  split_str = str.split("-")
  get_sections(split_str[0].to_i, split_str[1].to_i)
end

def part_1
  overlap_count = 0
  File.foreach(ARGV[0]) do |line|
    split_line = line.strip.split(',')
    assignment1 = split_line[0]
    assignment2 = split_line[1]
    assignment1_list = parse_sections(assignment1)
    assignment2_list = parse_sections(assignment2)
  
    if (assignment1_list - assignment2_list).empty? || (assignment2_list - assignment1_list).empty?
      overlap_count += 1
    end
  end
  puts "Part 1: #{overlap_count}"
end

def part_2
  overlap_count = 0
  File.foreach(ARGV[0]) do |line|
    split_line = line.strip.split(',')
    assignment1 = split_line[0]
    assignment2 = split_line[1]
    assignment1_list = parse_sections(assignment1)
    assignment2_list = parse_sections(assignment2)
  
    if (assignment1_list - assignment2_list).length < assignment1_list.length || (assignment2_list - assignment1_list).length < assignment2_list.length
      overlap_count += 1
    end
  end
  puts "Part 2: #{overlap_count}"
end

part_1
part_2
