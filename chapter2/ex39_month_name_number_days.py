"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""

month = input("Enter a month: ")

if month == "February":
    print(f"{month} has 28 or 29 days")
elif month in ("April", "June", "September", "November"):
    print(f"{month} has 30 days")
else:
    print(f"{month} has 31 days")
