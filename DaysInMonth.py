# File: DaysInMonth.py
# Student: Jennifer Truong
# UT EID: jat5244
# Course Name: CS303E
# 
# Date Created: 2/6/2021
# Date Last Modified: 2/10/2021
# Description of Program: Computing the user's input of numbers into days in a month


month = eval(input("Enter Month: "))
year = eval(input("Enter Year: "))
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#if-elif statements for months with 31 dayss
def main():
    if month == 1:
        print("January" , year , "has 31 days")
    elif month == 3:
        print("March" , year , "has 31 days")
    elif month == 5:
        print("May" , year , "has 31 days")
    elif month == 7:
        print("July" , year , "has 31 days")
    elif month == 8:
        print("August" , year , "has 31 days")
    elif month == 10:
        print("October" , year , "has 31 days")
    elif month == 12:
        print("December" , year , "has 31 days")

#if-elif statements for months with 30 days
    elif month == 4:
        print("April" , year , "has 30 days")
    elif month == 6:
        print("June" , year , "has 30 days")
    elif month == 9:
        print("September" , year , "has 30 days")
    elif month == 11:
        print("November" , year , "has 30 days")
    
#Calculating if the user's input is a leap year and the month for February
    else:
        if month == 2 and isLeapYear:
            print( "February" , year , "has 29 days")
        elif month == 2:
            print( "February" , year , "has 28 days")
        else:
            print("ERROR: Please input reasonable integers for the month and year.")

main()
