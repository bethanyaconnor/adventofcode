import sys

def read_lines_from_file():
  f = open(sys.argv[1], 'r')
  return f.readlines()

def read_2d_array_from_file():
  f = open(sys.argv[1], 'r')
  return [list(line.strip()) for line in f.readlines()]

def print_solution(part, solution):
  print("Part " + str(part) + ": " + str(solution))