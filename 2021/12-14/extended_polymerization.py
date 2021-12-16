import sys

def process_step(polymer, rules):
    new_polymer = polymer[0]
    for i in range(len(polymer)-1):
        first_char = polymer[i]
        second_char = polymer[i+1]
        if rules.get(first_char + second_char):
            new_polymer += rules[first_char + second_char]
        new_polymer += second_char
    return new_polymer


def part_1(start, rules):
    polymer = start
    for i in range(10):
        polymer = process_step(polymer, rules)
    char_frequency_map = {}
    most_frequency = 0
    least_frequency = len(polymer) + 1
    for c in list(polymer):
        if char_frequency_map.get(c):
            char_frequency_map[c] += 1
        else:
            char_frequency_map[c] = 1
    for count in char_frequency_map.values():
        if count > most_frequency:
            most_frequency = count
        if count < least_frequency:
            least_frequency = count
    return most_frequency - least_frequency


def process_pair(pair, rules, count, char_frequency_map):
    new_pair = pair
    for j in range(count):
        new_pair = process_step(new_pair, rules)
    expanded_pair = new_pair[1:-1]
    for c in list(expanded_pair):
        if char_frequency_map.get(c):
            char_frequency_map[c] += 1
        else:
            char_frequency_map[c] = 1
    return expanded_pair

def part_2(start, rules):
    pair_count_map = {}
    for i in range(len(start) - 1):
        pair = start[i] + start[i+1]
        if pair_count_map.get(pair):
            pair_count_map[pair] += 1
        else:
            pair_count_map[pair] = 1
    for c in range(40):
        new_pair_count_map = {}
        for pair in pair_count_map.keys():
            inserted_letter = rules[pair]
            new_pair_1 = pair[0] + inserted_letter
            new_pair_2 = inserted_letter + pair[1]
            if new_pair_count_map.get(new_pair_1):
                new_pair_count_map[new_pair_1] += pair_count_map[pair]
            else:
                new_pair_count_map[new_pair_1] = pair_count_map[pair]
            if new_pair_count_map.get(new_pair_2):
                new_pair_count_map[new_pair_2] += pair_count_map[pair]
            else:
                new_pair_count_map[new_pair_2] = pair_count_map[pair]
        pair_count_map = new_pair_count_map
    most_frequency = 0
    least_frequency = None
    char_frequency_map = {}
    for pair in pair_count_map.keys():
        char = pair[0]
        if char_frequency_map.get(char):
            char_frequency_map[char] += pair_count_map[pair]
        else:
            char_frequency_map[char] = pair_count_map[pair]
    char_frequency_map[start[-1]] += 1
    for count in char_frequency_map.values():
        if count > most_frequency:
            most_frequency = count
        if least_frequency == None or count < least_frequency:
            least_frequency = count
    return most_frequency - least_frequency

f = open(sys.argv[1], 'r')
start = f.readline().strip()
f.readline()
rules = {}
for x in f:
    rule = x.strip().split(' -> ')
    rules[rule[0].strip()] = rule[1].strip()

print("Part 1: " + str(part_1(start, rules)))
print("Part 2: " + str(part_2(start, rules)))

