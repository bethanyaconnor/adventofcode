import sys

f = open("input.txt", "r")
preamble_length = 25
last_digits = []
print("Part 1:")
for x in f:
  if len(last_digits) < preamble_length:
    last_digits.append(int(x))
  else:
    pair_found = False
    for i in range(0, preamble_length-1):
      if pair_found:
        break
      for j in range(i+1, preamble_length):
        if last_digits[i] + last_digits[j] == int(x):
          pair_found = True
          break
    if not pair_found:
      print(int(x))
      break
    else:
      last_digits.append(int(x))
      last_digits.pop(0)

f = open("input.txt", "r")
invalid_number = 22406676
digits = []
print("Part 2:")
for x in f:
  digits.append(int(x))
for i in range(0, len(digits)):
  sum = digits[i]
  current_digits = [digits[i]]
  for j in range(i+1, len(digits)):
    sum += digits[j]
    current_digits.append(digits[j])
    if sum == invalid_number:
      current_digits.sort()
      print(current_digits[0] + current_digits[-1])
      sys.exit(0)
    elif sum > invalid_number:
      break
