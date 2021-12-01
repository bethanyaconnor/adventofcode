


#starting_numbers = [3,1,2]
starting_numbers = [0,5,4,1,10,14,7]

last_seen = {}
for i in range(0, len(starting_numbers)-1):
    last_seen[str(starting_numbers[i])] = i+1
if starting_numbers[-1] in last_seen:
    next_num = len(starting_numbers) - last_seen[str(starting_numbers[-1])]
else:
    next_num = 0
last_seen[str(starting_numbers[-1])] = len(starting_numbers)

for i in range(len(starting_numbers)+1, 30000000):
    if str(next_num) in last_seen:
        current_num = next_num
        next_num = i - last_seen[str(current_num)]
        last_seen[str(current_num)] = i
    else:
        last_seen[str(next_num)] = i
        next_num = 0
print(next_num)
