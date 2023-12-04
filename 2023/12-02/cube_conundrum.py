import sys
sys.path.append('2023')
from util import read_lines_from_file, print_solution


def part_1(lines):
  sum_of_possible_game_ids = 0

  max_red = 12
  max_green = 13
  max_blue = 14

  for line in lines:
    line = line.split(':')
    game_num = int(line[0].split(' ')[1])
    sets = line[1].split(';')
    for single_set in sets:
      counts = single_set.strip().split(',')
      possible = True
      for single_ball_count in counts:
        [num, color] = single_ball_count.strip().split(' ')
        if color == 'red' and int(num) > max_red:
          possible = False 
          break
        elif color == 'green' and int(num) > max_green:
          possible = False 
          break
        elif color == 'blue' and int(num) > max_blue:
          possible = False 
          break
      if not possible:
        break
    if possible:
      sum_of_possible_game_ids += game_num
  print_solution(1, sum_of_possible_game_ids)

def part_2(lines):
  sum_of_game_powers = 0

  for line in lines:
    max_red = 0
    max_green = 0
    max_blue = 0

    line = line.split(':')
    game_num = int(line[0].split(' ')[1])
    sets = line[1].split(';')

    for single_set in sets:
      counts = single_set.strip().split(',')
      for single_ball_count in counts:
        [num, color] = single_ball_count.strip().split(' ')
        if color == 'red':
          max_red = max(max_red, int(num))
        elif color == 'green':
          max_green = max(max_green, int(num))
        elif color == 'blue':
          max_blue = max(max_blue, int(num))
    
    game_power = max_red * max_green * max_blue
    sum_of_game_powers += game_power
  print_solution(2, sum_of_game_powers)
   


lines = read_lines_from_file()
part_1(lines)
part_2(lines)