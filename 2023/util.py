import sys

def read_lines_from_file():
  f = open(sys.argv[1], 'r')
  return f.readlines()

def print_solution(part, solution):
  print("Part " + str(part) + ": " + str(solution))