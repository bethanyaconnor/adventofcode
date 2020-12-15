
class BoatAndWaypoint:
    def __init__(self):
        self.boat = Boat()
        self.x_from_boat = 10
        self.y_from_boat = 1

    def move(self, direction, value):
        if direction == 'N':
            self.y_from_boat += value
        elif direction == 'S':
            self.y_from_boat -= value
        elif direction == 'E':
            self.x_from_boat += value
        elif direction == 'W':
            self.x_from_boat -= value
        else:
            print('unknown direction')

    def do_instruction(self, action, value):
        cardinal_directions = ['N', 'E', 'S', 'W']
        if action == 'F':
            for i in range(0, value):
                self.boat.move('E', self.x_from_boat)
                self.boat.move('N', self.y_from_boat)
        elif action == 'R':
            if value == 90:
                temp_x = self.x_from_boat
                self.x_from_boat = self.y_from_boat
                self.y_from_boat = -1 * temp_x
            elif value == 180:
                self.x_from_boat = -1 * self.x_from_boat
                self.y_from_boat = -1 * self.y_from_boat
            elif value == 270:
                temp_x = self.x_from_boat
                self.x_from_boat = -1 * self.y_from_boat
                self.y_from_boat = temp_x
            else:
                print('unknown rotation')
        elif action == 'L':
            if value == 270:
                temp_x = self.x_from_boat
                self.x_from_boat = self.y_from_boat
                self.y_from_boat = -1 * temp_x
            elif value == 180:
                self.x_from_boat = -1 * self.x_from_boat
                self.y_from_boat = -1 * self.y_from_boat
            elif value == 90:
                temp_x = self.x_from_boat
                self.x_from_boat = -1 * self.y_from_boat
                self.y_from_boat = temp_x
            else:
                print('unknown rotation')
        else:
            self.move(action, value)


class Boat:
    def __init__(self):
        self.direction = 'E'
        self.x = 0
        self.y = 0

    def move(self, direction, value):
        if direction == 'N':
            self.y += value
        elif direction == 'S':
            self.y -= value
        elif direction == 'E':
            self.x += value
        elif direction == 'W':
            self.x -= value
        else:
            print('unknown direction')

    def do_instruction(self, action, value):
        cardinal_directions = ['N', 'E', 'S', 'W']
        if action == 'F':
            self.move(self.direction, value)
        elif action == 'R':
            self.direction = cardinal_directions[(cardinal_directions.index(self.direction) + value / 90) % 4]
        elif action == 'L':
            self.direction = cardinal_directions[(cardinal_directions.index(self.direction) - value / 90) % 4]
        else:
            self.move(action, value)

f = open("input.txt", "r")
boat = Boat()
waypoint = BoatAndWaypoint()
for x in f:
    boat.do_instruction(x[0], int(x[1:]))
    waypoint.do_instruction(x[0], int(x[1:]))
print("Part 1 answer: {}".format(abs(boat.x) + abs(boat.y)))
print("Part 2 answer: {}".format(abs(waypoint.boat.x) + abs(waypoint.boat.y)))
