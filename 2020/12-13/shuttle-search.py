def find_next_bus(current_time, bus_ids):
    next_bus = 0
    next_time = None
    for bus in bus_ids:
        dividend = current_time / bus
        bus_next_time = (dividend + 1) * bus
        if next_time == None or bus_next_time < next_time:
            next_bus = bus
            next_time = bus_next_time

    return (next_bus, next_time)

def find_max(bus_id_pairs):
    max_bus = bus_id_pairs[0]
    for bus_pair in bus_id_pairs:
        if bus_pair[0] > max_bus[0]:
            max_bus = bus_pair
    return max_bus

def find_bus_position_pairs(bus_ids):
    pairs = []
    for i in range(0, len(bus_ids)):
        if bus_ids[i] == 'x':
            continue
        pairs.append((int(bus_ids[i]), i))
    return pairs

def find_consecutive_bus_times(bus_ids, minimum = None):
    bus_pairs = find_bus_position_pairs(bus_ids)
    max_bus_pair = find_max(bus_pairs)
    if minimum == None:
        multiplier = 1
    else:
        multiplier = minimum / max_bus_pair[0] + 1
    print(multiplier)
    while True:
        current_earliest = multiplier * max_bus_pair[0] - max_bus_pair[1]
        multiplier += 1
        correct = True
        for bus in bus_pairs:
            if ((current_earliest + bus[1]) % bus[0]) != 0:
                correct = False
                break
        if correct:
            return current_earliest


lines = open("input.txt", "r").read().split('\n')
current_time = int(lines[0].strip())
bus_ids = map(lambda x: int(x), filter(lambda x: x != 'x', lines[1].strip().split(',')))
(next_bus, next_time) = find_next_bus(current_time, bus_ids)
print("Part 1 answer: {}".format(next_bus * (next_time - current_time)))
print("Part 2 answer: {}".format(find_consecutive_bus_times(lines[1].strip().split(','), 100000000000000)))
