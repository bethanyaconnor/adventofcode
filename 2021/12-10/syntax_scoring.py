import sys

ILLEGAL_CHARACTER_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

ADDED_CHARACTER_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}



CLOSE_TO_OPEN_MAP = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

OPEN_TO_CLOSE_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def find_corrupted_score(lines):
    score = 0
    for line in lines:
        stack = []
        for i in range(len(line)):
            if line[i] in ['(', '[', '{', '<']:
                stack.append(line[i])
            else:
                if stack[-1] == CLOSE_TO_OPEN_MAP[line[i]]:
                    stack.pop()
                else:
                    score += ILLEGAL_CHARACTER_SCORE[line[i]]
                    break
    return score

def find_autocomplete_score(lines):
    scores = []
    for line in lines:
        stack = []
        corrupted = False
        for i in range(len(line)):
            if line[i] in ['(', '[', '{', '<']:
                stack.append(line[i])
            else:
                if stack[-1] == CLOSE_TO_OPEN_MAP[line[i]]:
                    stack.pop()
                else:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while len(stack) > 0:
                open_char = stack.pop()
                close_char = OPEN_TO_CLOSE_MAP[open_char]
                score = (score * 5) + ADDED_CHARACTER_SCORE[close_char]
            scores.append(score)
    scores.sort()
    return scores[int(len(scores) / 2)]
    

f = open(sys.argv[1], 'r')
lines = []
for x in f:
    lines.append(x.strip())

print("Part 1: " + str(find_corrupted_score(lines)))
print("Part 2: " + str(find_autocomplete_score(lines)))

