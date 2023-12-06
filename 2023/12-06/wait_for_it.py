import sys
sys.path.append('2023')
from util import print_solution, read_lines_from_file

def num_ways_to_win(time, distance):
  min_hold_time = time + 1
  max_hold_time = 0

  for j in range(time+1):
    if (time - j) * j > distance:
      min_hold_time = j
      break
  for j in range(time, 0, -1):
    if (time - j) * j > distance:
      max_hold_time = j
      break
    
  return max_hold_time - min_hold_time + 1

def part_1(lines):
  times = list(map(int, lines[0].split(':')[1].strip().split()))
  distances = list(map(int, lines[1].split(':')[1].strip().split()))

  product_of_ways = 1

  for i in range(len(times)):
    time = times[i]
    distance = distances[i]
      
    num_ways = num_ways_to_win(time, distance)
    # print("For race " + str(i) + ", there are " + str(num_ways) + " ways to hold the button.")
    product_of_ways *= num_ways

  print_solution(1, product_of_ways)

    
def part_2(lines):
  time = int(''.join(lines[0].split(':')[1].strip().split()))
  distance = int(''.join(lines[1].split(':')[1].strip().split()))
  print_solution(2, num_ways_to_win(time, distance))

lines = read_lines_from_file()
part_1(lines)
part_2(lines)
