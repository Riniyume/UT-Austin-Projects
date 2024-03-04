#  File: GraphFill.py
#  Description: Program to generate the adjacency matrix of a graph and
#               implement Breadth-First Search and Depth-First Search to flood
#               fill pixels in images.
#  Student Name: Marilyn Shen
#  Student UT EID: mys467
#  Partner Name: Jennifer Truong
#  Partner UT EID: jat5244
#  Course Name: CS 313E
#  Unique Number: 51130
#  Date Created: 4/3/2022
#  Date Last Modified: 4/9/2022

import os
import sys

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"


# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if color not in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text


# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color) * 2, end='')


# Stack class; you can use this for your search algorithms
class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


# Queue class; you can use this for your search algorithms
class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# class for a graph node; contains x and y coordinates, a color, a list of
# edges and a flag signaling if the node has been visited (useful for search
# algorithms) it also contains a "previous color" attribute. This might be
# useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, x, y, color):
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to
    # in the node list. function adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)
        self.edges.sort()

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your
    # flood fill implementation)
    def set_color(self, color):
        self.prev_color = self.color
        self.color = color


# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size
        self.stack = Stack()

    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for _ in range(self.image_size)] for _ in
               range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()

        # print new line/reset color
        print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False

    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):
        print("Adjacency matrix:")

        # creates an nxn matrix and tests for adjacency between each node
        for row in range(len(self.nodes)):
            for col in range(len(self.nodes)):
                # 1 is connected edges, 0 is otherwise
                if col in self.nodes[row].edges:
                    print(1, end="")
                else:
                    print(0, end="")
            print("")

        # empty line afterwards
        print()

    # implement your bfs algorithm here. Call print_image() after coloring a
    # node. Input: graph is the graph containing the nodes, start_index is the
    # index of the currently visited node, color is the color to fill the area
    # containing the current node with
    def bfs(self, start_index, color):
        # reset visited status
        self.reset_visited()

        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()

        # create the queue and push the starting node into it
        bfs_queue = Queue()
        self.nodes[start_index].visited = True
        bfs_queue.enqueue(self.nodes[start_index])

        # primary function to create the queue and print the images in order
        while not bfs_queue.is_empty():
            # dequeues first object in queue, sets new color, and prints it
            node = bfs_queue.dequeue()
            node.set_color(color)
            self.print_image()

            # iterates through each adjacent node and enqueues it if it has not
            # been queued yet and matches the correct color
            for edge in node.edges:
                if self.nodes[edge].visited is False and \
                        self.nodes[edge].color == node.prev_color:
                    self.nodes[edge].visited = True
                    bfs_queue.enqueue(self.nodes[edge])

    # implement your dfs algorithm here. Call print_image() after coloring a
    # node Input: graph is the graph containing the nodes start_index is the
    # index of the currently visited node color is the color to fill the area
    # containing the current node with
    def dfs(self, start_index, color):
        # reset visited status
        self.reset_visited()

        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        # create stack & path, then mark index visited
        the_stack = Stack()
        path = []
        self.nodes[start_index].visited = True

        # insert start_index in stack
        if start_index not in the_stack.stack:
            the_stack.push(start_index)

        while not the_stack.is_empty():
            node = the_stack.pop()
            # to check if the visited node is already in the path
            if node in path:
                continue
            path.append(node)

            # change the color of node and print image
            self.nodes[node].set_color(color)
            self.print_image()

            # push all neighbors of the node into stack
            # that are not visited and have same previous color
            for edge in reversed(self.nodes[node].edges):
                if self.nodes[edge].visited is False and \
                        self.nodes[edge].color == self.nodes[node].prev_color:
                    the_stack.push(edge)


def main():
    # read the input file
    line = sys.stdin.readline()
    line = line.strip()

    # create the Graph object
    graph = ImageGraph(int(line))

    # first line of input tells us how many nodes we are using
    line = sys.stdin.readline()
    node_amount = int(line.strip())

    # creates the nodes using the specifics of the file
    for line in range(node_amount):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split(",")
        line[2] = line[2].replace(" ", "")
        graph.nodes.append(ColorNode(int(line[0]), int(line[1]), line[2]))

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # creates adjacency connection between the nodes
    for line in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split(",")

        # labeling the to and from nodes
        node_from = graph.nodes[int(edge[0])]
        node_to = graph.nodes[int(edge[1])]
        node_from.add_edge(int(edge[1]))
        node_to.add_edge(int(edge[0]))

    # print matrix
    graph.print_adjacency_matrix()

    # node index to start the BFS algorithms
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split(",")
    bfs_start = int(line[0])
    bfs_color = line[1]

    # run bfs
    graph.bfs(bfs_start, bfs_color)

    # node index to start the DFS algorithms
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split(",")
    dfs_start = int(line[0])
    dfs_color = line[1]

    # run dfs
    graph.dfs(dfs_start, dfs_color)


if __name__ == "__main__":
    main()
