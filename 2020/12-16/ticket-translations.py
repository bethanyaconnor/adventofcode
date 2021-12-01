import re
import copy

class Rule:
    def __init__(self, field, min1, max1, min2, max2):
        self.field = field
        self.min1 = int(min1)
        self.max1 = int(max1)
        self.min2 = int(min2)
        self.max2 = int(max2)

    def validate(self, value):
        return (value >= self.min1 and value <= self.max1) or (value >= self.min2 and value <= self.max2)

f = open('input.txt', 'r')
mode = 'rules'
rules = []
my_ticket = []
nearby_tickets = []
for x in f:
    if len(x.strip()) == 0:
        continue
    if x.strip() == 'your ticket:':
        mode = 'your ticket'
        continue
    if x.strip() == 'nearby tickets:':
        mode = 'nearby tickets'
        continue
    if mode == 'rules':
        regex = re.compile(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)")
        match = regex.match(x.strip())
        rules.append(Rule(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5)))
    elif mode == 'your ticket':
        my_ticket = x.strip().split(',')
    elif mode == 'nearby tickets':
        nearby_tickets.append(x.strip().split(','))

invalid_field_sum = 0
valid_tickets = []
for ticket in nearby_tickets:
    valid_ticket = True
    for field in ticket:
        valid_field = False
        for rule in rules:
            if rule.validate(int(field)):
                valid_field = True
        if not valid_field:
            invalid_field_sum += int(field)
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(ticket)
print(invalid_field_sum)

possible_rules = [None]*len(my_ticket)
for i in range(0, len(my_ticket)):
    possible_rules[i] = map(lambda x: x.field, rules)
for rule in rules:
    for i in range(0, len(my_ticket)):
        for ticket in valid_tickets:
            if rule.field in possible_rules[i] and not rule.validate(int(ticket[i])):
                possible_rules[i].remove(rule.field)
rule_data = [None]*len(my_ticket)
for i in range(0, len(my_ticket)):
    r = possible_rules[i]
    #print(map(lambda x: x.field, r))
    #print(len(r))
    rule_data[i] = (r, i)
rule_data.sort(key=lambda x: len(x[0]))
fields_with_rules = [None]*len(my_ticket)
for r, i in rule_data:
    for idx_r in fields_with_rules:
        if idx_r and idx_r in r:
            r.remove(idx_r)
    fields_with_rules[i] = r[0]
print fields_with_rules
product = 1
for i in range(0, len(fields_with_rules)):
    if fields_with_rules[i].startswith('departure'):
        print int(my_ticket[i])
        product *= int(my_ticket[i])
print(product)
