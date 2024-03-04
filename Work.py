#  File: Work.py

#  Description: Program to determine how many lines of code Chris has to write
#               before his first cup of coffee, as well as the time it would
#               take to determine this value through linear and binary searches

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3/01/2022

#  Date Last Modified: 3/01/2022
import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    the_sum, p = 0, 0
    while (v // k ** p) > 0:
        the_sum += v // k ** p
        p += 1
    return the_sum


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n, k):
    # go backwards from n for efficiency
    for v in range(n, 0, -1):
        if sum_series(v, k) == n:
            return v
        elif sum_series(v, k) < n:
            return v + 1


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    left = 0
    right = n
    while left <= right:
        middle_term = int((left + right) / 2)
        working_sum = sum_series(middle_term, k)

        # compare middle term sum with n to either return or create new middle
        if working_sum >= n > sum_series(middle_term - 1, k):
            return middle_term
        elif working_sum < n:
            left = middle_term + 1
        else:
            right = middle_term - 1


def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()
