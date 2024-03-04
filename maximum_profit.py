#  File: maximum_profit.py

#  Description: Gives the max profit result that an investor can sell
#               a specific amount of houses next year using the knapsack dynamic
#               programming algorithm.

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 4/25/2022

#  Date Last Modified: 4/26/2022
import sys


# Add Your functions here

# {money} is the total investment, {prices} is the list of house prices.
# returns a list of all sets of houses that are equal to or less than {money}
def knapsack_algorithm(max_price, prices, values, house_count):
    # create an array of size max_price x house_count
    dynamic_arr = [[0 for _ in range(max_price + 1)]
                   for _ in range(house_count + 1)]

    # Build table dynamic_array[][] in bottom up manner
    for i in range(house_count + 1):
        for w in range(max_price + 1):
            if i == 0 or w == 0:
                dynamic_arr[i][w] = 0
            elif prices[i - 1] <= w:
                dynamic_arr[i][w] = max(values[i - 1] +
                                        dynamic_arr[i - 1][w - prices[i - 1]],
                                        dynamic_arr[i - 1][w])
            else:
                dynamic_arr[i][w] = dynamic_arr[i - 1][w]

    return dynamic_arr[house_count][max_price]

# You are allowed to change the main function.

# Do not change the template file name. 


def main():
    # The first line is the amount of investment in million USD which is an
    # integer number
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)

    # The second line includes an integer number which is the number of houses
    # listed for sale
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    # The third line is a list of house prices in million dollar which is a list
    # of {integer numbers} (Consider that house prices can be an integer number
    # in million dollar only)
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])

    # Add your implementation here

    # value_list is the "true value" of each house
    value_list = [increase[x] * prices[x] / 100 for x in range(len(prices))]

    # Add your functions and call them to generate the result in two decimal
    # spots.

    result = round(knapsack_algorithm(money, prices, value_list, num_houses), 2)

    print(result)


main()
