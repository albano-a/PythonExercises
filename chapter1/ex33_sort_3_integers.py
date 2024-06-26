"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""

integer = input("Enter 3 integers: ")

summation = int(integer[0]) + int(integer[1]) + int(integer[2])

minimum = min(integer)
middle = summation - int(min(integer)) - int(max(integer))
maximum = max(integer)


print(minimum, middle, maximum)
