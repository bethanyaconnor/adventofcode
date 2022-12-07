
class PlainFile
  def initialize(name, size)
    @name = name
    @size = size.to_i
  end

  def name
    @name
  end

  def size
    @size
  end
end

class Directory
  # name
  # children
  def initialize(name, parent=nil)
    @name = name
    @children = []
    @parent = parent
    @size = nil
  end

  def add_child(obj)
    @children.append(obj)
  end

  def children
    @children
  end

  def parent
    @parent
  end

  def name
    @name
  end

  def find_child(name)
    @children.find {|c| c.name == name }
  end

  def size
    return @size if @size
    @size = @children.reduce(0) { |sum, child| sum + child.size }
  end
end

def create_file_system
  lines = File.readlines(ARGV[0])
  root = Directory.new('/')
  current_directory = root

  list_mode = false
  lines.each do |line|
    line.strip!
    if line.start_with?('$ ')
      list_mode = false
      line = line[2..-1]
      if line.start_with?('cd')
        if line == 'cd /'
          current_directory = root
        elsif line == 'cd ..'
          current_directory = current_directory.parent
        else
          new_directory_name = line[3..-1]
          existing_directory = current_directory.find_child(new_directory_name)
          if existing_directory
            current_directory = existing_directory
          else
            new_directory = Directory.new(new_directory_name, parent=current_directory)
            current_directory.add_child(new_directory)
            current_directory = new_directory
          end
        end
      else
        list_mode = true
      end
    else
      split_line = line.split(' ')
      if split_line[0] == 'dir'
        current_directory.add_child(Directory.new(split_line[1], parent=current_directory))
      else
        current_directory.add_child(PlainFile.new(split_line[1], split_line[0]))
      end
    end
  end
  root
end

def find_size_sum_1(node)
  return_val = 0
  if node.size < 100000
    return_val += node.size
  end
  node.children.each do |child|
    if child.is_a?(Directory)
      return_val += find_size_sum_1(child)
    end
  end
  return_val
end

def find_deletion_candidates(node, min_size)
  candidates = []
  if node.size >= min_size
    candidates.append(node)
  end
  node.children.each do |child|
    if child.is_a?(Directory)
      candidates += find_deletion_candidates(child, min_size)
    end
  end
  candidates
end

def part_1(root)
  puts "Part 1: #{find_size_sum_1(root)}"
end

def part_2(root)
  total_space_available = 70000000
  current_space_used = root.size
  current_free_space = total_space_available - current_space_used
  needed_free_space = 30000000
  additional_needed_free_space = needed_free_space - current_free_space

  deletion_candidates = find_deletion_candidates(root, additional_needed_free_space)
  deletion_candidates.sort_by! {|c| c.size }
  puts "Part 2: #{deletion_candidates[0].size}"
end

root = create_file_system
part_1(root)
part_2(root)
