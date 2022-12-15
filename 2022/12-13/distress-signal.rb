
require 'json'

EQUAL = 0
CORRECT = 1
INCORRECT = -1

def packet_order_correct?(packet1, packet2)
  packet1.each_with_index do |val1, idx|
    return INCORRECT if idx >= packet2.length
    val2 = packet2[idx]
    #puts "Comparing #{val1.inspect} with #{val2.inspect}"
    if val1.is_a?(Integer) && val2.is_a?(Integer)
      return CORRECT if val1 < val2
      return INCORRECT if val1 > val2
    elsif val1.is_a?(Integer)
      res = packet_order_correct?([val1], val2)
      return res unless res == EQUAL
    elsif val2.is_a?(Integer)
      res = packet_order_correct?(val1, [val2])
      return res unless res == EQUAL
    else
      res = packet_order_correct?(val1, val2)
      return res unless res == EQUAL
    end
  end
  return CORRECT if packet1.length < packet2.length
  return EQUAL
end

def parse_packet_str(packet_str)
  packet = []
  current_arr = []
  chars = packet_str[1...-1].split('')
  chars.each do |char|
    if char == ']'
      packet.append(current_arr)
      current_arr = []
    elsif char != '['
    end
  end
end

#puts packet_order_correct?([1,1,3,1,1], [1,1,5,1,1])
#puts packet_order_correct?([[1],[2,3,4]], [[1],4])
#puts packet_order_correct?([9], [[8,7,6]])
#puts packet_order_correct?([[4,4],4,4], [[4,4],4,4,4])
#puts packet_order_correct?([7,7,7,7], [7,7,7])
#puts packet_order_correct?([], [3])
#puts packet_order_correct?([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])

correct_packet_idx_sum = 0
lines = File.readlines(ARGV[0]).map(&:strip)
lines_idx = 0
pairs_idx = 1
all_packets = []
while lines_idx < lines.length
  packet1 = JSON.parse(lines[lines_idx])
  packet2 = JSON.parse(lines[lines_idx+1])
  all_packets.append(packet1)
  all_packets.append(packet2)
  correct_packet_idx_sum += pairs_idx unless packet_order_correct?(packet1, packet2) == INCORRECT
  lines_idx += 3
  pairs_idx += 1
end
puts "Part 1: #{correct_packet_idx_sum}"

all_packets.append([[2]])
all_packets.append([[6]])
sorted_packets = all_packets.sort {|a,b| packet_order_correct?(b, a)}
puts "Part 2: #{(sorted_packets.find_index([[2]])+1) * (sorted_packets.find_index([[6]])+1)}"

