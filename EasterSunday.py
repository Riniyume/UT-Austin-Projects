# File: EasterSunday.py
# Student: Jennifer Truong
# UT EID: jat5244
# Course: CS303E
# 
# Date Created: 1/30/2021
# Date Last Modified: 1/31/2021
# Description of Program: Computes the date of Easter Sunday in a specific year.


# Print the user's input
year = eval(input("Enter year: "))


# The calculations/ algorithm for Easter Sunday
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25 
h = (19 * a + b -d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32


# The print statement of computing the date for Easter Sunday
print("In" , year , "Easter Sunday is on month" , n , "and day" , p)
