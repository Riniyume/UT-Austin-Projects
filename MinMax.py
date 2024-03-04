# File: MinMax.py
# Student: Jennifer Truong
# UT EID: Jat5244
# Course Name: CS303E
# 
# Date Created: 2/21/2021
# Date Last Modified: 2/24/2021
# Description of Program: A program that will print out the minimum and maximum of the arbitrary number of integers the user had inputted.


# Storing the information and informing the user to put in integer(s)
integerInputValue = input("Enter an integer or 'stop' to end: ")
if integerInputValue == 'stop':
    print("You didn't enter any numbers")
    integerValue = integerInputValue
else:
    integerValue = int(integerInputValue)
    maximum = integerValue
    minimum = integerValue
# The loop to allow the user to do as many inputs as they want until they stop
while integerInputValue != 'stop':
# Breaking the loop
    integerInputValue = input("Enter an integer or 'stop' to end: ")
    if integerInputValue == 'stop':
        print("The maximum is" , maximum)
        print("The minimum is" , minimum)
        break
# Switching the maximum and minimum, if necessary, when the user inputs a new integer
    else:
        integerValue = int(integerInputValue)
        
        if integerValue < minimum:
            minimum = integerValue
        elif integerValue > maximum:
            maximum = integerValue
