"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""

from math import pi

c_radius: float = 3.0
c_height: float = 5.0

volume: float = pi * c_radius**2 * c_height

print(
    f"The volume of a cylinder with radius {c_radius}m and height {c_height}m is {volume:.1f}m³"
)
