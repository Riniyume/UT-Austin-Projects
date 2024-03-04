#  File: ExpressionTree.py

#  Description: Algorithm to evaluate a given expression and determine its
#               postfix and prefix expressions.

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3/13/2022

#  Date Last Modified: 3/23/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


# stack used to store operators when building tree
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None
        self.pre_answer = []
        self.post_answer = []

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        tokens = expr.split()
        expr_stack = Stack()
        self.root = current_node = Node()

        # parse the expression and assign values to expression tree
        for token in tokens:

            # each "(" denotes the beginning of an expression
            if token == "(":
                current_node.lChild = Node()
                expr_stack.push(current_node)
                current_node = current_node.lChild

            # each ")" denotes the end of an expression
            elif token == ")":
                if not expr_stack.is_empty():
                    current_node = expr_stack.pop()

            # assigns operators to proper nodes
            elif token in operators:
                current_node.data = token
                expr_stack.push(current_node)
                current_node.rChild = Node()
                current_node = current_node.rChild

            # assigns operands to proper nodes
            else:
                current_node.data = token
                current_node = expr_stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    # recursive function performed on each parent node
    def evaluate(self, aNode):

        # when only the root node is left, returns the answer
        if aNode.lChild is None and aNode.rChild is None:
            return float(aNode.data)

        # evaluates the left and right children
        left_exp = self.evaluate(aNode.lChild)
        right_exp = self.evaluate(aNode.rChild)

        # perform the operation of the root onto the operands
        # operators = ['+', '-', '*', '/', '//', '%', '**']
        if aNode.data == "+":
            return left_exp + right_exp
        elif aNode.data == "-":
            return left_exp - right_exp
        elif aNode.data == "*":
            return left_exp * right_exp
        elif aNode.data == "/":
            return left_exp / right_exp
        elif aNode.data == "//":
            return left_exp // right_exp
        elif aNode.data == "%":
            return left_exp % right_exp
        elif aNode.data == "**":
            return left_exp ** right_exp

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    # order: parent lChild rChild
    def pre_order(self, aNode):
        if not aNode:
            return
        self.pre_answer.append(str(aNode.data))
        self.pre_order(aNode.lChild)
        self.pre_order(aNode.rChild)
        return ' '.join(self.pre_answer)

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    # order: lChild rChild parent
    def post_order(self, aNode):
        if not aNode:
            return
        self.post_order(aNode.lChild)
        self.post_order(aNode.rChild)
        self.post_answer.append(str(aNode.data))
        return ' '.join(self.post_answer)


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root))

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root))


if __name__ == "__main__":
    main()
