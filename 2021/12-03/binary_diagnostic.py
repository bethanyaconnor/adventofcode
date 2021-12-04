
import sys

def get_counts(report):
    one_counts = None
    zero_counts = None
    for x in report:
        x = x.strip()
        if one_counts == None:
            one_counts = [0]*len(x)
            zero_counts = [0]*len(x)
        for i in range(len(x)):
            if x[i] == '0':
                zero_counts[i] += 1
            elif x[i] == '1':
                one_counts[i] += 1
            else:
                print("don't know what to do with " + x[i])
    return [zero_counts, one_counts]

def get_gamma_epsilon(report):
    [zero_counts, one_counts] = get_counts(report)
    gamma = ""
    epsilon = ""
    for i in range(len(one_counts)):
        if one_counts[i] >= zero_counts[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return [gamma, epsilon]


def find_oxygen_generator_rating(report):
    remaining_set = report
    gamma = get_gamma_epsilon(remaining_set)[0]
    for i in range(len(gamma)):
        new_set = []
        for j in range(len(remaining_set)):
            if remaining_set[j][i] == gamma[i]:
                new_set.append(remaining_set[j])
        remaining_set = new_set
        if len(remaining_set) == 1:
            return remaining_set[0]
        gamma = get_gamma_epsilon(remaining_set)[0]
    print("couldn't find oxygen generator rating")
    return remaining_set[0]

def find_co2_scrubber_rating(report):
    remaining_set = report
    epsilon = get_gamma_epsilon(remaining_set)[1]
    for i in range(len(epsilon)):
        new_set = []
        for j in range(len(remaining_set)):
            if remaining_set[j][i] == epsilon[i]:
                new_set.append(remaining_set[j])
        remaining_set = new_set
        if len(remaining_set) == 1:
            return remaining_set[0]
        epsilon = get_gamma_epsilon(remaining_set)[1]
    print("couldn't find oxygen generator rating")
    return remaining_set[0]


def part_1(report):
    [gamma, epsilon] = get_gamma_epsilon(report)
    return (int(gamma, 2) * int(epsilon, 2))

def part_2(report):
    oxygen_generator = find_oxygen_generator_rating(report)
    co2_scrubber_rating = find_co2_scrubber_rating(report) 
    return (int(oxygen_generator,2) * int(co2_scrubber_rating, 2))

f = open(sys.argv[1], "r")
report = []
for x in f:
    report.append(x)

print("Part 1: " + str(part_1(report)))
print("Part 2: " + str(part_2(report)))
