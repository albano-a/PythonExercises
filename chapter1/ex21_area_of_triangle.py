"""
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:

Write a program that allows the user to enter values for b and h. The program should
then compute and display the area of a triangle with base length b and height h
"""

base = float(input("Enter a value for the base: "))
height = float(input("Enter a value for the height: "))

area = (base * height) / 2

print(f"The area of the triangle is equal to {area}meters")
