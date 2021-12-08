import sys

def part_1(displays):
    num_easy = 0
    for display in displays:
        [signals, output] = display.split(' | ')
        output_values = output.split()
        for value in output_values:
            if len(value) in [2, 3, 4, 7]:
                num_easy += 1
    return num_easy

def part_2(displays):
    output_sum = 0
    for display in displays:
        [signals, outputs] = display.split(' | ')
        signals = list(map(lambda s : ''.join(sorted(s)), signals.split()))
        output_values = list(map(lambda s : ''.join(sorted(s)), outputs.split()))
        signals_by_length = {}
        signal_to_num = {}
        for signal in signals:
            if signals_by_length.get(len(signal)):
                signals_by_length[len(signal)].append(signal)
            else:
                signals_by_length[len(signal)] = [signal]
            if len(signal) == 2:
                signal_to_num[signal] = 1
            if len(signal) == 3:
                signal_to_num[signal] = 7
            if len(signal) == 4:
                signal_to_num[signal] = 4
            if len(signal) == 7:
                signal_to_num[signal] = 8
        segment_map = {}
        for c in signals_by_length[3][0]:
            if c in signals_by_length[2][0]:
                continue
            segment_map['a'] = c
        four_leftovers = []
        for c in signals_by_length[4][0]:
            if c in signals_by_length[2][0]:
                continue
            four_leftovers.append(c)
        assert(len(four_leftovers) == 2)
        for fives in signals_by_length[5]:
            if signals_by_length[2][0][0] in fives and signals_by_length[2][0][1] in fives:
                signal_to_num[fives] = 3
            elif four_leftovers[0] in fives and four_leftovers[1] in fives:
                signal_to_num[fives] = 5
            else:
                signal_to_num[fives] = 2
        for six in signals_by_length[6]:
            if signals_by_length[4][0][0] in six and signals_by_length[4][0][1] in six and signals_by_length[4][0][2] in six and signals_by_length[4][0][3] in six:
                signal_to_num[six] = 9
            elif signals_by_length[3][0][0] in six and signals_by_length[3][0][1] in six and signals_by_length[3][0][2] in six:
                signal_to_num[six] = 0
            else:
                signal_to_num[six] = 6
        output = ""
        assert(sorted(signal_to_num.values()) == [0,1,2,3,4,5,6,7,8,9])
        for value in output_values:
            output += str(signal_to_num[value])
        output_sum += int(output)
    return output_sum

f = open(sys.argv[1], 'r')
displays = []
for x in f:
    displays.append(x.strip())

print("Part 1: " + str(part_1(displays)))
print("Part 2: " + str(part_2(displays)))

