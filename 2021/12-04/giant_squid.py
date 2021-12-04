import sys

def card_has_bingo(card):
    for row in card:
        if all(n == None for n in row):
            return True
    for i in range(5):
        if card[0][i] == None and card[1][i] == None and card[2][i] == None and card[3][i] == None and card[4][i] == None:
            return True
    return False

def find_first_winning_card(cards, draws):
    for draw in draws:
        for card in cards:
            for col in range(5):
                for row in range(5):
                    if card[col][row] == draw:
                        card[col][row] = None
            if card_has_bingo(card):
                return [card, draw]
    return [None, None]

def find_last_winning_card(cards, draws):
    remaining_cards = cards
    for draw in draws:
        cards_to_remove = []
        for card in remaining_cards:
            for col in range(5):
                for row in range(5):
                    if card[col][row] == draw:
                        card[col][row] = None
            if card_has_bingo(card):
                if len(remaining_cards) == 1:
                    return [card, draw]
                cards_to_remove.append(card)
        for card in cards_to_remove:
            remaining_cards.remove(card)
    return [None, None]

def score_winning_card(card, last_draw):
    unmarked_sum = 0
    for col in range(5):
        for row in range(5):
            if card[col][row] != None:
                unmarked_sum += int(card[col][row])
    return unmarked_sum * int(last_draw)

def part_1(cards, draw):
    [first_winning_card, last_draw] = find_first_winning_card(cards, draw)
    return score_winning_card(first_winning_card, last_draw)

def part_2(cards, draw):
    [last_winning_card, last_draw] = find_last_winning_card(cards, draw)
    return score_winning_card(last_winning_card, last_draw)

f = open(sys.argv[1], "r")
draws = []
bingo_cards = []
line_num = 0
current_card = []
for x in f:
    if line_num == 0:
        draws = x.strip().split(',')
    elif line_num == 1:
        pass
    elif len(x.strip()) == 0:
        bingo_cards.append(current_card)
        current_card = []
    else:
        current_card.append(x.strip().split())
    line_num += 1
bingo_cards.append(current_card)

print("Part 1: " + str(part_1(bingo_cards, draws)))
print("Part 2: " + str(part_2(bingo_cards, draws)))
