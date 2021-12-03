
import sys

f = open(sys.argv[1], "r")
one_counts = None
zero_counts = None
gamma = ""
epsilon = ""
for x in f:
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
for i in range(len(one_counts)):
    if one_counts[i] > zero_counts[i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))

#print("Part 1: " + str(find_increases(measurements)))
#print("Part 2: " + str(find_window_increases(measurements)))
