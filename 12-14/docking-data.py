import re
import copy

def apply_mask(num, mask):
    binary = list('{0:036b}'.format(num))
    for i in range(0,36):
        if mask[i] != 'X':
            binary[i] = mask[i]
    return int(''.join(binary), 2)

def apply_mask_to_address(address, mask):
    binary = list('{0:036b}'.format(address))
    for i in range(0,36):
        if mask[i] != '0':
            binary[i] = mask[i]
    possible_addresses = [''.join(binary)]
    for i in range(0,36):
        new_possible_addresses = copy.deepcopy(possible_addresses)
        for addr in possible_addresses:
            if addr[i] == 'X':
                new_possible_addresses.remove(addr)
                bits = list(addr)
                bits[i] = '0'
                new_possible_addresses.append(''.join(bits))
                bits[i] = '1'
                new_possible_addresses.append(''.join(bits))
        possible_addresses = copy.deepcopy(new_possible_addresses)
    return map(lambda x: int(x, 2), possible_addresses)

f = open("input.txt", "r")
mem = {}
mem2 = {}
mask = 'X'*36
for x in f:
    parts = x.strip().split(' = ')
    if parts[0] == 'mask':
        mask = parts[1]
    else:
        match = re.search(r"mem\[(\d+)\]", parts[0])
        if not match:
            print("no match found!")
        else:
            mem[match[1]] = apply_mask(int(parts[1]), mask)
            addresses = apply_mask_to_address(int(match[1]), mask)
            for address in addresses:
                mem2[str(address)] = int(parts[1])
mem_sum = 0
for key, value in mem.items():
    mem_sum += value
print("Part 1 solution is {}".format(mem_sum))
mem_sum2 = 0
for key, value in mem2.items():
    mem_sum2 += value
print("Part 2 solution is {}".format(mem_sum2))

