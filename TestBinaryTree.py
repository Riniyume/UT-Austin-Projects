#  File: TestBinaryTree.py

# Description: Program to create a binary search tree, and perform functions:
#               range(), get_level(), left_side_view(), and sum_leaf_nodes()

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3/23/2022

#  Date Last Modified: 3/30/2022


import sys


class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild is not None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild is not None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild is not None and self.rChild is not None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild is not None:
            return 1 + self.lChild.get_height()
        elif self.rChild is not None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None
        self.total = 0

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr is not None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparison to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree
    # minus the minimum value. If there is one value in the tree the range is 0.
    # If the tree is empty the range is undefined.
    def range(self):
        maximum = int(self.max(self.root).data)
        minimum = int(self.min(self.root).data)
        if self.root is None:
            return None
        else:
            return maximum - minimum

    # maximum is found by going to the rightmost node
    def max(self, aNode):
        if not aNode.rChild:
            return aNode
        else:
            return self.max(aNode.rChild)

    # finding the minimum by leftmost node
    def min(self, aNode):
        if not aNode.lChild:
            return aNode
        else:
            return self.min(aNode.lChild)

    # helper function for get_level. traverses the tree and returns values if
    # they are at the correct level
    # level = levels left before correct level
    def traverse_tree(self, aNode, level):
        # if at the correct level, return the node
        if level == 0:
            return [aNode]
        # if lChild and rChild exist, recurse lChild and rChild of aNode
        if aNode.lChild and aNode.rChild:
            return self.traverse_tree(aNode.lChild, level - 1) + \
                   self.traverse_tree(aNode.rChild, level - 1)
        # if only lChild exists, recurse lChild of aNode
        elif aNode.lChild:
            return self.traverse_tree(aNode.lChild, level - 1)
        # if only rChild exists, recurse rChild of aNode
        elif aNode.rChild:
            return self.traverse_tree(aNode.rChild, level - 1)
        # if neither lChild or rChild exist, return nothing
        else:
            return []

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        # if tree is empty, return nothing
        if not self.root:
            return []
        # if level asked for does not exist, return nothing
        if level >= self.get_height():
            return []
        # use recursion helper function to find values
        return self.traverse_tree(self.root, level)

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        answer = []
        # append the leftmost value of every level to answer
        for level in range(self.get_height()):
            answer.append(self.get_level(level)[0].data)
            level += 1
        return answer

    # a helper function for sum_leaf_nodes
    def sum_leaf_helper(self, aNode):
        # if it's empty
        if aNode is None:
            return
        # if leaf node add the node's data to the sum counter
        elif aNode.lChild is None and aNode.rChild is None:
            self.total += aNode.data
        # recurse the function until it's done
        else:
            self.sum_leaf_helper(aNode.lChild)
            self.sum_leaf_helper(aNode.rChild)

        return self.total

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        # run through helper function to generate nodes
        return self.sum_leaf_helper(self.root)


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ", t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

    # Another Tree for test
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ", t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")

    # Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ", t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
