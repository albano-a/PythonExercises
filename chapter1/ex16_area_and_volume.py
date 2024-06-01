"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""

from math import pi

_radius = float(input("Enter a radius value (m): "))

area_circle = pi * _radius**2
volume_sphere = (4 / 3) * pi * _radius**3

print(f"The area of a circle with radius {_radius} is {area_circle:.2f}m")
print(f"The volume of a sphere with radius {_radius}m is {volume_sphere:.2f}m")
