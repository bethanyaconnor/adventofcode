import sys
sys.path.append('2023')
from util import read_lines_from_file, print_solution
import re

def find_calibration_value_digits(line):
  char_list = list(line)
  first_digit = -1
  last_digit = -1
  for char in char_list:
    if str.isdigit(char):
      first_digit = char
      break
  for char in reversed(char_list):
    if str.isdigit(char):
      last_digit = char
      break
  return int(first_digit + last_digit)

def str_to_num_str(string):
  if string == 'one':
    return '1'
  elif string == 'two':
    return '2'
  elif string == 'three':
    return '3'
  elif string == 'four':
    return '4'
  elif string == 'five':
    return '5'
  elif string == 'six':
    return '6'
  elif string == 'seven':
    return '7'
  elif string == 'eight':
    return '8'
  elif string == 'nine':
    return '9'
  elif string.isdigit():
    return string
  else:
    throw("Invalid string: " + string)

def find_calibration_value_regex(line):
  # Some hacky nonsense from: https://stackoverflow.com/questions/5616822/how-to-use-regex-to-find-all-overlapping-matches
  regex = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
  matches = regex.findall(line)
  first_digit = str_to_num_str(matches[0])
  last_digit = str_to_num_str(matches[-1])
  # print(line + " produces a calibration value of " + first_digit + last_digit)
  print(line.strip() + ',' + first_digit + last_digit)
  return int(first_digit + last_digit)

def part_1(lines):
  sum_of_calibration_values = 0
  for line in lines:
    sum_of_calibration_values += find_calibration_value_digits(line)
  print_solution(1, sum_of_calibration_values) 

def part_2(lines):
  sum_of_calibration_values = 0
  for line in lines:
    sum_of_calibration_values += find_calibration_value_regex(line)
  print_solution(2, sum_of_calibration_values)

lines = read_lines_from_file()
part_1(lines)
part_2(lines)

