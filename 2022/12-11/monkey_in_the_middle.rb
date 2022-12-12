
class Monkey
  attr_accessor :num, :items, :inspection_count

  def initialize(num, operation, test_dividend, true_monkey, false_monkey, starting_items)
    @num = num
    @operation = operation.strip.split(' ')
    @test_dividend = test_dividend
    @true_monkey = true_monkey
    @false_monkey = false_monkey
    @items = starting_items
    @inspection_count = 0
  end

  def test(worry_level)
    @inspection_count += 1
    return @true_monkey if worry_level % @test_dividend == 0
    return @false_monkey
  end

  def operation(worry_level)
    left_num = (@operation[0] == 'old' ? worry_level : @operation[0].to_i)
    right_num = (@operation[2] == 'old' ? worry_level : @operation[2].to_i)
    if @operation[1] == '+'
      left_num + right_num
    elsif @operation[1] == '-'
      left_num - right_num
    elsif @operation[1] == '*'
      left_num * right_num
    else
      left_num / right_num
    end
  end
end

class Item
  attr_accessor :worry_level, :current_monkey

  def initialize(worry_level)
    @worry_level = worry_level.to_i
    @current_monkey = nil
  end
end

def parse_input
  input_lines = File.readlines(ARGV[0]).map(&:strip)
  idx = 0
  monkey_list = []
  while idx < input_lines.length
    monkey_num = input_lines[idx].split(' ')[-1].to_i
    starting_items = input_lines[idx+1].split(':')[-1].split(',').map {|w| Item.new(w.strip.to_i) }
    operation = input_lines[idx+2].split('=')[-1].strip
    test_dividend = input_lines[idx+3].split(' ')[-1].to_i
    true_monkey = input_lines[idx+4].split(' ')[-1].to_i
    false_monkey = input_lines[idx+5].split(' ')[-1].to_i
    monkey_list[monkey_num] = Monkey.new(monkey_num, operation, test_dividend, true_monkey, false_monkey, starting_items)
    monkey_list[monkey_num].items.each {|i| i.current_monkey = monkey_list[monkey_num] }
    idx += 7
  end
  monkey_list
end

def part_1(monkey_list)
  starting_time = Time.now
  (1..20).each do |round_num|
    monkey_list.each do |monkey|
      monkey.items.each do |item|
        new_item_worry_level = item.worry_level
        new_item_worry_level = monkey.operation(new_item_worry_level)
        new_item_worry_level /= 3
        item.worry_level = new_item_worry_level
        monkey_list[monkey.test(new_item_worry_level).to_i].items.append(item)
      end
      monkey.items = []
    end
    #puts "After Round #{round_num}:"
    #monkey_list.each do |monkey|
    #  puts "Monkey #{monkey.num}: #{monkey.items.map(&:worry_level).inspect}"
    #end
  end
  top_monkey = nil
  monkey_list.each do |monkey|
    unless top_monkey
      top_monkey = monkey
    else
        top_monkey = monkey if monkey.inspection_count > top_monkey.inspection_count
    end
  end
  second_monkey = nil
  monkey_list.each do |monkey|
    unless monkey.num == top_monkey.num
      unless second_monkey
        second_monkey = monkey
      else
        second_monkey = monkey if monkey.inspection_count > second_monkey.inspection_count
      end
    end
  end
  puts "Part 1: #{top_monkey.inspection_count * second_monkey.inspection_count}"
  ending_time = Time.now
  puts "Elapsed: #{ending_time - starting_time}"
end

def part_2(monkey_list)
  (1..10000).each do |round_num|
    monkey_list.each do |monkey|
      monkey.items.each do |item|
        new_item_worry_level = item.worry_level
        new_item_worry_level = monkey.operation(new_item_worry_level)
        item.worry_level = new_item_worry_level
        monkey_list[monkey.test(new_item_worry_level).to_i].items.append(item)
      end
      monkey.items = []
    end
    if round_num % 100 == 0
     puts "After Round #{round_num}:"
     monkey_list.each do |monkey|
       puts "Monkey #{monkey.num}: #{monkey.items.map(&:worry_level).inspect}"
     end
    end
  end
  top_monkey = nil
  monkey_list.each do |monkey|
    unless top_monkey
      top_monkey = monkey
    else
        top_monkey = monkey if monkey.inspection_count > top_monkey.inspection_count
    end
  end
  second_monkey = nil
  monkey_list.each do |monkey|
    unless monkey.num == top_monkey.num
      unless second_monkey
        second_monkey = monkey
      else
        second_monkey = monkey if monkey.inspection_count > second_monkey.inspection_count
      end
    end
  end
  puts "Part 2: #{top_monkey.inspection_count * second_monkey.inspection_count}"
end

def part_2_2(monkey_list)
  item_list = monkey_list.map(&:items).flatten
  item_list.each do |item|
    (1..20).each do
      monkey = item.current_monkey
      new_item_worry_level = item.worry_level
      new_item_worry_level = monkey.operation(new_item_worry_level)
      new_item_worry_level /= 3
      item.worry_level = new_item_worry_level
      item.current_monkey = monkey_list[monkey.test(new_item_worry_level).to_i]
    end
  end

  top_monkey = nil
  monkey_list.each do |monkey|
    unless top_monkey
      top_monkey = monkey
    else
        top_monkey = monkey if monkey.inspection_count > top_monkey.inspection_count
    end
  end
  second_monkey = nil
  monkey_list.each do |monkey|
    unless monkey.num == top_monkey.num
      unless second_monkey
        second_monkey = monkey
      else
        second_monkey = monkey if monkey.inspection_count > second_monkey.inspection_count
      end
    end
  end
  puts "Part 2: #{top_monkey.inspection_count * second_monkey.inspection_count}"
end


monkey_list = parse_input
part_1(monkey_list.dup)
monkey_list = parse_input
#part_2(monkey_list.dup)
#part_2_2(monkey_list.dup)
