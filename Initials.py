# File: Initials.py
# Student: Jennifer Truong
# UT EID: jat5244
# Course: CS303E
# 
# Date Created: 1/21/2020
# Date Last Modified: 1/23/2020
# Description of Program: This prints out my initials, J.A.T, in large letters.

# All of the variables listed to make the image of initials
twoJ = "JJ"
sixJ = twoJ + twoJ + twoJ
twelveJ = twoJ + twoJ + twoJ + twoJ + twoJ + twoJ
twoA = "AA"
fourA = twoA + twoA
eightA = twoA + twoA + twoA + twoA
twoT = "TT"
twelveT = twoT + twoT + twoT + twoT + twoT + twoT
period = ".."
space = "  "
threeSpace = space + " "
quadSpace = space + space
sixSpace = quadSpace + space
sevenSpace = sixSpace + " "
eightSpace = quadSpace + quadSpace
tenSpace = eightSpace + space
twelveSpace = eightSpace + quadSpace


# defining separate functions to print out an individual lines with minimum repetition
def lineOfOne():
    print(space + twelveJ + tenSpace + fourA + eightSpace + space + twelveT)
    print(space + twelveJ + tenSpace + fourA + eightSpace + space + twelveT)
    
def lineOfTwo():
    print(sevenSpace + twoJ + twelveSpace + space + twoA + space + twoA + twelveSpace + space + twoT)
    
def lineOfThree():
    print(sevenSpace + twoJ + twelveSpace + " " + eightA + twelveSpace + " " + twoT)
    print(sevenSpace + twoJ + twelveSpace + " " + eightA + twelveSpace + " " + twoT)

def lineOfFour():
    print(threeSpace + twoJ + space + twoJ + twelveSpace + twoA + sixSpace + twoA + twelveSpace + twoT)
    print(threeSpace + twoJ + space + twoJ + twelveSpace + twoA + sixSpace + twoA + twelveSpace + twoT)

def lineOfFive():
    print(threeSpace + sixJ + sevenSpace + period + space + twoA + eightSpace + twoA + space + period + sevenSpace + twoT + sevenSpace + period + space)
    print(threeSpace + sixJ + sevenSpace + period + space + twoA + eightSpace + twoA + space + period + sevenSpace + twoT + sevenSpace + period + space)


# printing out the initials
print()
lineOfOne()
lineOfTwo()
lineOfThree()
lineOfFour()
lineOfFive()
print()


