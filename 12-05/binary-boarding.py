import math

def find_row(seat_code):
    min_row = 0
    max_row = 127
    for i in range(0, 6):
        mid_point = math.floor((min_row + max_row) / 2)
        if seat_code[i] == 'F':
            max_row = mid_point
        else:
            min_row = mid_point + 1
    if seat_code[6] == 'F':
        return min_row
    else:
        return max_row

def find_column(seat_code):
    min_column = 0
    max_column = 7
    for i in range(7, 9):
        mid_point = math.floor((min_column + max_column) / 2)
        if seat_code[i] == 'L':
            max_column = mid_point
        else:
            min_column = mid_point + 1
    if seat_code[9] == 'L':
        return min_column
    else:
        return max_column

f = open("input.txt", "r")
#max_seat_id = 0
occupied_seats = [False] * 1025
for x in f:
    row = find_row(x)
    column = find_column(x)
    seat_id = row * 8 + column
    occupied_seats[seat_id] = True
    #if seat_id > max_seat_id:
    #    max_seat_id = seat_id
#print(max_seat_id)
for i in range(1, 1024):
    if not occupied_seats[i] and occupied_seats[i-1] and occupied_seats[i+1]:
        print(i)
        break
