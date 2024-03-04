#  File: Spiral.py

# Description: For each of the numbers inside the spiral of the parameter given, outputs the sum of all
#              the numbers adjacent to the given number, but not including the number itself.

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 1/25/2022

#  Date Last Modified: 2/02/2022

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys


def create_spiral(n):
    arr = [[0] * n for _ in range(n)]
    addend = [(-1, 0), (0, 1), (1, 0), (0, -1)]     # add coordinates to arr[x][y] to get location of next number
    direction = 0
    x, y = int((n - 1) / 2), int((n - 1) / 2)       # start in the middle of the array

    for i in range(1, n ** 2 + 1):
        arr[x][y] = i
        new_x, new_y = x + addend[direction][0], y + addend[direction][1]

        # check to see if we can change direction without overwriting a previous value
        dir_x, dir_y = x + addend[(direction + 1) % 4][0], y + addend[(direction + 1) % 4][1]
        if arr[dir_x][dir_y] == 0:
            direction = (direction + 1) % 4
            new_x, new_y = x + addend[direction][0], y + addend[direction][1]

        x, y = new_x, new_y     # reassigning new indices

    # outline the array with zeroes to eradicate errors when computing sum in sum_adjacent_numbers
    arr.insert(0, [0] * n)
    arr.append([0] * n)
    for r in range(0, n + 2):
        arr[r].insert(0, 0)
        arr[r].append(0)

    return arr


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0


def sum_adjacent_numbers(spiral, n):
    x = None
    y = None
    answer = -n

    # for loop to find indices of n
    for index, lst in enumerate(spiral):
        if n in lst:
            x = index
            y = lst.index(n)

    # nested for loop adds every number in 3x3 square surrounding n
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            answer += spiral[i][j]

    return answer


def main():
    # read the input file
    data = sys.stdin.read()
    data_split = data.split("\n")
    ans = []

    # convert str to int and remove blank line at the end of the file
    for i in range(0, len(data_split)):
        if data_split[i] == "":
            data_split.pop(i)
        else:
            data_split[i] = int(data_split[i])

    # create the spiral
    spiral = create_spiral(data_split[0])

    # add the adjacent numbers
    for i in range(1, len(data_split)):
        ans.append(sum_adjacent_numbers(spiral, data_split[i]))

    # print the result
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
