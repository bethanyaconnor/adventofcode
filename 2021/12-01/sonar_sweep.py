
import sys

def find_increases(measurements):
    last_x = None
    num_increases = 0
    for x in measurements:
        if last_x != None and int(x) > last_x:
            num_increases += 1
        last_x = int(x)
    return num_increases

def find_window_increases(measurements):
    window_sums = [0]*len(measurements)
    for i in range(len(measurements)):
        if i - 2 > 0:
            window_sums[i-2] += measurements[i]
        if i - 1 > 0:
            window_sums[i - 1] += measurements[i]
        window_sums[i] += measurements[i]
    return find_increases(window_sums[0:-2])

f = open(sys.argv[1], "r")
measurements = []
for x in f:
    measurements.append(int(x))

print("Part 1: " + str(find_increases(measurements)))
print("Part 2: " + str(find_window_increases(measurements)))
