import sys

def process_lanternfish_slow(ages, days):
    current_ages = ages
    for day in range(days):
        new_ages = []
        for l in current_ages:
            if l == 0:
                new_ages.append(8)
                new_ages.append(6)
            else:
                new_ages.append(l-1)
        current_ages = new_ages
    return len(current_ages)

def process_lanternfish_mem(ages_list, days):
    current_ages = [0]*9
    for age in ages_list:
        current_ages[age] += 1
    for day in range(days):
        new_ages = []
        new_ages.append(current_ages[1]) # 0
        new_ages.append(current_ages[2]) # 1
        new_ages.append(current_ages[3]) # 2
        new_ages.append(current_ages[4]) # 4
        new_ages.append(current_ages[5]) # 4
        new_ages.append(current_ages[6]) # 5
        new_ages.append(current_ages[0] + current_ages[7]) # 6
        new_ages.append(current_ages[8]) # 7
        new_ages.append(current_ages[0]) # 8
        current_ages = new_ages
    return sum(current_ages)

f = open(sys.argv[1], "r")
starting_ages = []
for x in f:
    starting_ages = x.split(',')
starting_ages = list(map(lambda s : int(s), starting_ages))

print("Part 1 (slow): " + str(process_lanternfish_slow(starting_ages, 80)))
print("Part 1 (mem): " + str(process_lanternfish_mem(starting_ages, 80)))
print("Part 2: " + str(process_lanternfish_mem(starting_ages, 256)))
