
class Adaptor:
    def __init__(self, voltage):
        self.voltage = voltage
        self.possible_connections = []
        self.connection_sum = None

    def add_possible_connections(self, adaptor):
        self.possible_connections.append(adaptor)

    def set_connection_sum(self, connection_sum):
        self.connection_sum = connection_sum


def count_combinations(adaptors):
    sum = 0
    for adaptor in adaptors:
        if not adaptor.connection_sum:
            if len(adaptor.possible_connections) == 0:
                adaptor.set_connection_sum(1)
            else:
                adaptor.set_connection_sum(
                    count_combinations(adaptor.possible_connections)
                )
        sum += adaptor.connection_sum
    return sum

f = open("input.txt", "r")
adaptor_ratings = []
for x in f:
    adaptor_ratings.append(int(x))
adaptor_ratings.sort()
jumps = {1: 0, 2: 0, 3: 1}
current_voltage = 0
for adaptor in adaptor_ratings:
    if adaptor > current_voltage + 3:
        print ("cannot use more adaptors")
    else:
        jumps[adaptor-current_voltage] += 1
        current_voltage = adaptor
print("The answer to part 1 is " + str(jumps[1] * jumps[3]))

adaptors = [Adaptor(0)]
for adaptor_rating in adaptor_ratings:
    adaptor = Adaptor(adaptor_rating)
    adaptors.append(adaptor)

for i in range(0, len(adaptors) - 1):
    parent_adaptor = adaptors[i]
    for j in range(i+1, len(adaptors)):
        if adaptors[j].voltage > parent_adaptor.voltage + 3:
            break
        parent_adaptor.add_possible_connections(adaptors[j])

combinations = count_combinations(adaptors[0].possible_connections)
print("The answer to part 2 is " + str(combinations))
