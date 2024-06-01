"""
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
"""

from math import pi, tan

s = float(input("Enter the length of the side: "))
n = int(input("Enter the number of sides: "))

area = (n * s**2) / (4 * tan(pi / n))

print(f"The area of a polygon with {n} sides is {area:.2f}m")
