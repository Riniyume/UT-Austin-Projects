# File: Payroll.py
# Student: Jennifer Truong
# UT EID: jat5244
# Course Name: CS303E
# Unique Number: XXXXX
# 
# Date Created: 1/31/2021
# Date Last Modified: 2/03/2021
# Description of Program: This program calculates and prints out a payroll statement based on the info the user provides.


# The user will input the info needed to calculate their payroll, and also variables listed

name = input("Enter employee's name: ")
numberOfHoursWorked = eval(input("Enter number of hours worked in a week: "))
hourlyPayRate = eval(input("hourly pay rate: "))
federalTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

# Calculating the payroll 
grossPay = numberOfHoursWorked * hourlyPayRate
federalTaxPercent = federalTax * 100
stateTaxPercent = stateTax * 100
federalWitholding = grossPay * federalTax
stateWithholding = grossPay * stateTax
netPay = grossPay - federalWitholding - stateWithholding
totalDeduction = federalWitholding + stateWithholding

# Print the information and also converts the numbers into strings statements
print()
print("Employee Name: " + name)
print("Hours Worked:" , float(numberOfHoursWorked))
print("Pay Rate: $" + str(round(hourlyPayRate , 2)))
print("Gross Pay: $" + str(format(grossPay , "5.2f")))
print("Deductions: ")
print("  Federal Withholding (" + str(round(federalTaxPercent, 2)) + "%): $" + str(format(federalWitholding, "5.2f")))
print("  State Withholding (" + str(round(stateTaxPercent , 2)) + "%): $" + str(round(stateWithholding , 2)))
print("  Total Deduction: $" + str(round(totalDeduction , 2)))
print("Net Pay: $" + str(round(netPay, 2)))
