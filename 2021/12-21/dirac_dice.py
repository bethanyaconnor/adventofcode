import sys

def part_1(player1_start, player2_start):
    player1_score = 0
    player2_score = 0
    player1_position = player1_start
    player2_position = player2_start

    rolls = 0
    current_dice = 1
    while True:
        player1_move = 0
        for i in range(3):
            #print(current_dice)
            player1_move += current_dice
            current_dice += 1
            if current_dice > 100:
                current_dice = 1
        rolls += 3
        player1_position += player1_move
        if player1_position > 10:
            player1_position = player1_position % 10
            if player1_position == 0:
                player1_position = 10
        player1_score += player1_position
        #print("Player 1 score: " + str(player1_score)) 
        if player1_score >= 1000:
            print("Player 1 won with " + str(player1_score) + " after " + str(rolls) + " rolls. Player 2 got " + str(player2_score))
            return player2_score * rolls
        player2_move = 0
        for i in range(3):
            #print(current_dice)
            player2_move += current_dice
            current_dice += 1
            if current_dice > 100:
                current_dice = 1
        rolls += 3
        player2_position += player2_move
        if player2_position > 10:
            player2_position = player2_position % 10
            if player2_position == 0:
                player2_position = 10
        player2_score += player2_position
        #print("Player 2 score: " + str(player2_score)) 
        if player2_score >= 1000:
            print("Player 2 won with " + str(player2_score) + " after " + str(rolls) + " rolls. Player 1 got " + str(player1_score))
            return player1_score * rolls

player1_start = int(sys.argv[1])
player2_start = int(sys.argv[2])

print("Part 1: " + str(part_1(player1_start, player2_start)))
