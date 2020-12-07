class Bag:
    def __init__(self, color):
        self.color = color
        self.inner_bags = []
        self.outer_bags = []
        self.visited = False

    def __repr__(self):
        return self.color + " has visited: " + str(self.visited)
        #return self.color + ": " + str(self.inner_bags)

    def set_visited(self):
        self.visited = True

    def add_inner_bag(self, inner_bag, quantity):
        self.inner_bags.append((inner_bag, quantity))
        inner_bag.add_outer_bag(self)

    def add_outer_bag(self, outer_bag):
        self.outer_bags.append(outer_bag);


def count_parents(bags, bag):
    count = 0
    for b in bag.outer_bags:
        if not b.visited:
            b.set_visited()
            count += 1
            count += count_parents(bags, b)
    return count

def count_children(bags, bag):
    count = 0
    for (b, quantity) in bag.inner_bags:
        count += quantity
        count += quantity * count_children(bags, b)
    return count

f = open("input.txt", "r")
rules = []
bags = {}
for x in f:
    rules.append(x.strip()[:-1])
    parts = x.strip()[:-1].split(' contain ')
    color = parts[0].split(' bags')[0]
    new_bag = Bag(color)
    bags[color] = new_bag
    
for rule in rules:
    parts = rule.split(' contain ')
    color = parts[0].split(' bags')[0]
    bag = bags[color]
    if parts[1] == 'no other bags':
        continue
    contained_bag_input = parts[1].split(',')
    for b in contained_bag_input:
        words = b.strip().split(' ')
        num_words = len(words)
        words = words[:-1]
        contained_color = ' '.join(words[1:])
        bag.add_inner_bag(bags[contained_color], int(words[0]))

#print(bags)
print(count_children(bags, bags['shiny gold']))
