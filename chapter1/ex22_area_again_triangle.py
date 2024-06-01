"""
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known.
Then the area of the triangle
can be calculated using the following formula:
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.
"""

from math import sqrt

side_1 = float(input("Enter a value for the side 1 of the triangle: "))
side_2 = float(input("Enter a value for the side 2 of the triangle: "))
side_3 = float(input("Enter a value for the side 3 of the triangle: "))

S = (side_1 + side_2 + side_3) / 2

area_tri = sqrt(S * (S - side_1) * (S - side_2) * (S - side_3))

print(f"The area of the triangle is equal to {area_tri:.2f}")
