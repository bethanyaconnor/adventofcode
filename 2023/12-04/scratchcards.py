import sys
sys.path.append('2023')
from util import read_lines_from_file, print_solution

def part_1(lines):
  point_sum = 0

  for line in lines:
    [winning_numbers, ticket_numbers] = line.split('|')
    winning_numbers = winning_numbers.split(':')[1].strip().split()
    ticket_numbers = ticket_numbers.strip().split()

    if len(ticket_numbers) != len(list(set(ticket_numbers))):
      print("Duplicate ticket numbers found in: " + str(line))

    num_wins = 0
    for ticket_number in ticket_numbers:
      if ticket_number in winning_numbers:
        num_wins += 1

    ticket_points = 0 if num_wins == 0 else pow(2, num_wins - 1) 
    # print(line.strip() + ' | ' + str(ticket_points))
    point_sum += ticket_points

  print_solution(1, point_sum)

def part_2(lines):
  total_cards = 0
  duplicates = dict()
  for line in lines:
    [winning_numbers, ticket_numbers] = line.split('|')
    #winning_numbers = winning_numbers.split(':')[1].strip().split()
    [case_num, winning_numbers] = winning_numbers.split(':')
    case_num = int(case_num.strip().split()[1])
    winning_numbers = winning_numbers.strip().split()
    ticket_numbers = ticket_numbers.strip().split()

    if len(ticket_numbers) != len(list(set(ticket_numbers))):
      print("Duplicate ticket numbers found in: " + str(line))

    num_wins = 0
    for ticket_number in ticket_numbers:
      if ticket_number in winning_numbers:
        num_wins += 1

    num_cards = 1 + duplicates.get(case_num, 0)
    # print(str(num_cards) + " of card " + str(case_num))
    for i in range(num_wins+1):
      duplicates[case_num + i] = duplicates.get(case_num + i, 0) + num_cards
    total_cards += num_cards
    # print(str(case_num) + ',' + str(num_wins))

  print_solution(2, total_cards)

lines = read_lines_from_file()
part_1(lines)
part_2(lines)