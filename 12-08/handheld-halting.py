import copy

def test_termination(instructions):
    acc = 0
    visited = [False]*len(instructions)
    line = 0
    while True:
        if line == len(instructions):
            return (True, acc)
        tokens = instructions[line].split(' ')
        if visited[line]:
            return (False, acc)
        visited[line] = True
        if tokens[0] == 'nop':
            line += 1
        elif tokens[0] == 'acc':
            line += 1
            acc += int(tokens[1])
        else:
            line += int(tokens[1])

def fix_program(instructions):
    for x in range(0, len(instructions)):
        if 'acc' in instructions[x]:
            continue
        copied_instructions = copy.deepcopy(instructions)
        if 'nop' in instructions[x]:
            copied_instructions[x] = instructions[x].replace('nop', 'jmp')
        else:
            copied_instructions[x] = instructions[x].replace('jmp', 'nop')
        (terminated, final_acc) = test_termination(copied_instructions)
        if terminated:
            return final_acc
    print("No solution found")
    return 0


def simulate_program(instructions):
    acc = 0
    visited = [False]*len(instructions)
    line = 0
    while True:
        tokens = instructions[line].split(' ')
        if visited[line]:
            return acc
        visited[line] = True
        if tokens[0] == 'nop':
            line += 1
        elif tokens[0] == 'acc':
            line += 1
            acc += int(tokens[1])
        else:
            line += int(tokens[1])


f = open("input.txt", "r")
instructions = []
for x in f:
    instructions.append(x.strip())
print("Part 1 answer: {}".format(simulate_program(instructions)))
print("Part 1 answer: {}".format(fix_program(instructions)))
