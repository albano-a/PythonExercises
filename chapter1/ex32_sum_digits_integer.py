"""
Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3 + 1 + 4 + 1 = 9.
"""

integer = input("Enter a integer: ")
a = int(integer[0])
b = int(integer[1])
c = int(integer[2])
d = int(integer[3])

total = a + b + c + d

print(f"The sum of all digits from {integer} is {total}")
