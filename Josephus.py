#  File: Josephus.py

#  Description: Algorithm to solve the Josephus problem!

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3/09/2022

#  Date Last Modified: 3/13/2022
import sys


class Link(object):
    # This class represents a link between data items only
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    # Insert an element (value) in the list
    def insert(self, data):
        new_node = Link(data)

        # if list is empty
        if self.last is None:
            self.last = new_node
            self.first = new_node
            new_node.next = self.first
        # if list is not already empty
        else:
            self.last.next = new_node
            self.last = new_node
            new_node.next = self.first

        self.size += 1

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.last

        # list is empty
        if current is None:
            return None
        # if the data is located at the head/tail of the node
        if self.last.data is data:
            return self.last

        # search and find the position of the given data, then get the link.
        next_node = self.first
        while next_node is not self.last:
            if next_node.data == data:
                return next_node
            next_node = next_node.next
        return None

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        # if list is empty
        if self.last is None:
            return None

        # if list has one value
        if self.last is self.first:
            self.first = None
            self.last = None
            return self.last

        current = self.first
        previous = self.last

        while current.data != data:
            if current is self.last:
                return None
            else:
                previous = current
                current = current.next

        # when current.data is data
        previous.next = current.next

        if current is self.first:
            self.first = previous.next

        if current is self.last:
            self.last = previous

        self.size -= 1

        return current

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):

        # find the starting point
        previous = self.find(start)
        current = previous.next

        # use n to determine deleted link(previous) and next link(current)
        while n > 1:
            previous = current
            current = current.next
            n -= 1

        # delete the link
        self.delete(previous.data)

        return previous, current

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        current = self.first
        string = []

        if self.first is None:
            return str(string)

        while current is not self.last:
            string.append(current.data)
            current = current.next

        string.append(self.last.data)

        return str(string)


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    soldier_list = CircularList()

    # add soldiers to circular list
    for soldier in range(1, num_soldiers + 1):
        soldier_list.insert(soldier)

    # print soldiers in order of death
    while soldier_list.size > 1:
        returned = soldier_list.delete_after(start_count, elim_num)
        print(returned[0])
        start_count = returned[1].data

    # print soldier who lives
    print(soldier_list.last)


if __name__ == "__main__":
    main()
