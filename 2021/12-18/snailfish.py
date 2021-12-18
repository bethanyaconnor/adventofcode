import sys
import math

class ExpressionNode:
    def __init__(self, parent, expression):
        self.expression = expression
        self.left_node = None
        self.right_node = None
        self.parent = parent
        try:
            self.num = int(expression)
        except ValueError:
            self.num = None
            node_expressions = []
            middle_index = None
            bracket_count = 0
            for i in range(1, len(expression) - 1):
                c = expression[i]
                if c == '[':
                    bracket_count += 1
                if c == ']':
                    bracket_count -= 1
                if c == ',' and bracket_count == 0:
                    middle_index = i
                    break
            left_expression = expression[1:middle_index]
            right_expression = expression[middle_index+1:-1]
            self.left_node = ExpressionNode(self, left_expression)
            self.right_node = ExpressionNode(self, right_expression)

    def to_string(self):
        return self.expression

    def calculate_expression(self):
        if self.num != None:
            return str(self.num)
        else:
            return "[" + self.left_node.calculate_expression() + "," + self.right_node.calculate_expression() + "]"

    def update_expression(self):
        self.expression = self.calculate_expression()

    def magnitude(self):
        if self.num != None:
            return self.num
        else:
            return 3 * self.left_node.magnitude() + 2 * self.right_node.magnitude()

    def print_node(self):
        if self.left_node:
            print("Value: " + self.expression + ", Left Node: " + self.left_node.to_string() + ", Right Node: " + self.right_node.to_string())
            self.left_node.print_node()
            self.right_node.print_node()
        else:
            print("Value: " + str(self.num))

    def split(self):
        left_value = math.floor(self.num / 2)
        right_value = math.ceil(self.num / 2)
        self.num = None
        self.expression = "[" + str(left_value) + "," + str(right_value) + "]"
        self.left_node = ExpressionNode(self, str(left_value))
        self.right_node = ExpressionNode(self, str(right_value))
        ancestor = self.parent
        while ancestor:
            ancestor.update_expression()
            ancestor = ancestor.parent

    def explode(self):
        left_value = self.left_node.num
        right_value = self.right_node.num
        grandparent = self.parent.parent
        #if grandparent.left_node != self.parent:
        #    left_node = grandparent.left_node
        #    while not left_node.num:
        #        left_node = left_node.left_node
        #    left_node.num += left_value
        #elif grandparent.parent:
        #    left_node = grandparent.parent.left_node
        #    while not left_node.num:
        #        left_node = left_node.left_node
        #if grandparent.right_node != self.parent:
        #    right_node = grandparent.right_node
        #    while not right_node.num:
        #        right_node = right_node.right_node
        #    right_node.num += right_value
        #elif grandparent.parent:
        #    right_node = grandparent.parent.right_node
        #    while not right_node.num:
        #        right_node = right_node.right_node
        parent_to_check = self.parent
        prev_parent = self
        while parent_to_check:
            node_for_left_value = parent_to_check.left_node
            if node_for_left_value != prev_parent:
                while node_for_left_value and node_for_left_value.num == None:
                    node_for_left_value = node_for_left_value.right_node
                if node_for_left_value:
                    node_for_left_value.num += left_value
                    break
            prev_parent = parent_to_check
            parent_to_check = parent_to_check.parent
        parent_to_check = self.parent
        prev_parent = self
        while parent_to_check:
            node_for_right_value = parent_to_check.right_node
            if node_for_right_value != prev_parent:
                while node_for_right_value and node_for_right_value.num == None:
                     node_for_right_value = node_for_right_value.left_node
                if node_for_right_value:
                    node_for_right_value.num += right_value
                    break
            prev_parent = parent_to_check
            parent_to_check = parent_to_check.parent
        self.expression = "0"
        self.num = 0
        self.left_node = None
        self.right_node = None
        ancestor = self.parent
        while ancestor:
            ancestor.update_expression()
            ancestor = ancestor.parent


def reduce_tree(root_node):
    done = False
    while not done:
        node_to_explode = None
        node_to_split = None
        depth_map = { root_node.expression: 0 }
        nodes_to_check = [root_node]
        while len(nodes_to_check) > 0:
            node = nodes_to_check.pop()
            node_depth = depth_map[node.expression]
            if node.num and node.num >= 10 and not node_to_split:
                node_to_split = node
            if node_depth >= 4 and node.num == None and not node_to_explode:
                node_to_explode = node
            if node.right_node:
                nodes_to_check.append(node.right_node)
                depth_map[node.right_node.expression] = node_depth + 1
            if node.left_node:
                nodes_to_check.append(node.left_node)
                depth_map[node.left_node.expression] = node_depth + 1
        if node_to_explode == None and node_to_split == None:
            done = True
        if node_to_explode:
            node_to_explode.explode()
        elif node_to_split:
            node_to_split.split()

def add_expressions(exp1, exp2):
    new_exp = "[" + exp1 + "," + exp2 + "]"
    node = ExpressionNode(None, new_exp)
    reduce_tree(node)
    return node.expression

def part_1(expressions_to_add):
    current_expression = expressions_to_add[0]
    for i in range(1, len(expressions_to_add)):
        current_expression = add_expressions(current_expression, expressions_to_add[i])

    final_expression_node = ExpressionNode(None, current_expression)
    print(final_expression_node.magnitude())

def part_2(expressions_to_add):
    largest_magnitude = 0
    for i in range(len(expressions_to_add)):
        for j in range(len(expressions_to_add)):
            if i == j:
                continue
            summed_expression = add_expressions(expressions_to_add[i], expressions_to_add[j])
            magnitude = ExpressionNode(None, summed_expression).magnitude()
            if magnitude > largest_magnitude:
                largest_magnitude = magnitude
    print(largest_magnitude)

f = open(sys.argv[1], 'r')
expressions_to_add = []
for x in f:
    expressions_to_add.append(x.strip())

#node = ExpressionNode(None, '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
#node = ExpressionNode(None, '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
#node = ExpressionNode(None, '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')

#node.print_node()
#reduce_tree(node)
#print(node.expression)

part_1(expressions_to_add)
part_2(expressions_to_add)
