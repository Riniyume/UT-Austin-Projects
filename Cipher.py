#  File: Cipher.py

# Description: decrypting and encrypting cipher string message

#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 2/03/2022

#  Date Last Modified: 2/09/2022

import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string


def encrypt(strng):

	# finding length for nxn message w/ padding of "*"
	length = len(strng)
	n = math.ceil(math.sqrt(length))
	new_string = strng + (n ** 2 - length) * "*"
	arr = []
	arr_final = [[""] * n for _ in range(n)]
	answer = str()

	# creating a list split into n
	while new_string:
		arr.append(new_string[:n])
		new_string = new_string[n:]

	# creating the 2d message
	for i in range(n):
		arr[i] = list(arr[i])

	# rotating the message 90 degrees clockwise
	for row in range(n):
		for column in range(n):
			arr_final[column][n - row - 1] = arr[row][column]

	# converting the 2d list into a string w/o "*"
	for row in range(n):
		for column in range(n):
			if arr_final[row][column] != "*":
				answer = answer + arr_final[row][column]

	return answer

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 


def decrypt(strng):

	# finding length for nxn message w/ padding of "*"
	length = len(strng)
	n = math.ceil(math.sqrt(length))
	stars = n ** 2 - length
	arr = [[""] * n for _ in range(n)]
	arr_final = [[""] * n for _ in range(n)]
	index = 0
	answer = str()

	# creating the padding for message
	for column in range(n):
		for row in range(n - 1, -1, -1):
			if stars < 1:
				break
			arr[row][column] = "*"
			stars -= 1
		if stars < 1:
			break

	# inserting the message w/ padding
	for row in range(n):
		for column in range(n):
			if arr[row][column] != "*":
				arr[row][column] = strng[index]
				index += 1

	# rotating the message 90 degrees counter-clockwise
	for row in range(n):
		for column in range(n):
			arr_final[n - column - 1][row] = arr[row][column]

	# converting the 2d list into a string w/o "*"
	for row in range(n):
		for column in range(n):
			if arr_final[row][column] != "*":
				answer = answer + arr_final[row][column]

	return answer


def main():

	# read the strings P and Q from standard input
	data = sys.stdin.read()
	data_split = data.split("\n")

	# encrypt the string P
	p = encrypt(data_split[0])

	# decrypt the string Q
	q = decrypt(data_split[1])

	# print the encrypted string of P
	print(p)

	# and the decrypted string of Q
	print(q)


if __name__ == "__main__":
	main()

