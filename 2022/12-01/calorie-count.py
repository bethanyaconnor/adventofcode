import sys

f = open(sys.argv[1], 'r')
calory_totals = []
running_total = 0
for x in f:
    if x.strip() == "":
        calory_totals.append(running_total)
        running_total = 0
    else:
        running_total += int(x)

calory_totals.append(running_total)
calory_totals.sort()

print("Part 1: " + str(calory_totals[-1]))
print("Part 2: " + str(calory_totals[-1] + calory_totals[-2] + calory_totals[-3]))
