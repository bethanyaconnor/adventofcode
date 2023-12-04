import sys
sys.path.append('2023')
from util import read_2d_array_from_file, print_solution

def part_1(grid):
  symbol_locations = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] != '.' and not grid[i][j].isdigit():
        symbol_locations.append((j, i))
    
  possible_part_numbers = []
  for i in range(len(grid)):
    current_part_number = ''
    current_part_number_start = None
    for j in range(len(grid[i])):
      if grid[i][j].isdigit():
        current_part_number += grid[i][j]
        if not current_part_number_start:
          current_part_number_start = j
      elif current_part_number != '':
        possible_part_numbers.append({'num': current_part_number, 'startX': current_part_number_start, 'endX': j - 1, 'y': i})
        current_part_number = ''
        current_part_number_start = None
    if current_part_number != '':
      possible_part_numbers.append({'num': current_part_number, 'startX': current_part_number_start, 'endX': len(grid[i]) - 1, 'y': i})

  part_number_sum = 0

  for possible_part_number in possible_part_numbers:
    for symbol_location in symbol_locations:
      if symbol_location[1] >= possible_part_number['y'] - 1 and symbol_location[1] <= possible_part_number['y'] + 1:
        if symbol_location[0] >= possible_part_number['startX'] - 1 and symbol_location[0] <= possible_part_number['endX'] + 1:
          part_number_sum += int(possible_part_number['num'])
          break
  
  print_solution(1, part_number_sum)

def part_2(grid):
  possible_part_numbers = []
  for i in range(len(grid)):
    current_part_number = ''
    current_part_number_start = None
    for j in range(len(grid[i])):
      if grid[i][j].isdigit():
        current_part_number += grid[i][j]
        if not current_part_number_start:
          current_part_number_start = j
      elif current_part_number != '':
        possible_part_numbers.append({'num': current_part_number, 'startX': current_part_number_start, 'endX': j - 1, 'y': i})
        current_part_number = ''
        current_part_number_start = None
    if current_part_number != '':
      possible_part_numbers.append({'num': current_part_number, 'startX': current_part_number_start, 'endX': len(grid[i]) - 1, 'y': i})

  gear_ratio_sum = 0
  possible_gear_locations = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == '*':
        num_adjacent_part_numbers = []
        for possible_part_number in possible_part_numbers:
          if i >= possible_part_number['y'] - 1 and i <= possible_part_number['y'] + 1:
            if j >= possible_part_number['startX'] - 1 and j <= possible_part_number['endX'] + 1:
              num_adjacent_part_numbers.append(possible_part_number)
        if len(num_adjacent_part_numbers) == 2:
          gear_ratio_sum += int(num_adjacent_part_numbers[0]['num']) * int(num_adjacent_part_numbers[1]['num'])
    
  print_solution(2, gear_ratio_sum)




grid = read_2d_array_from_file()
part_1(grid)
part_2(grid)