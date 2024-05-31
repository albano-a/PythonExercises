"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth's
surface. The distance between these points, following the surface of the Earth, in
kilometers is:

distance = 6371.01 * arcos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
"""

from math import acos, sin, cos, radians

t1, g1 = input("Enter the first point (latitude and longitude): ").split(" ")
t2, g2 = input("Enter the second point (latitude and longitude): ").split(" ")
t1, g1, t2, g2 = float(t1), float(g1), float(t2), float(g2)


distance = 6371.01 * acos(
    sin(radians(t1)) * sin(radians(t2))
    + cos(radians(t1)) * cos(radians(t2)) * cos(radians(g1) - radians(g2))
)


print(f"The distance between points {(t1, g1)} and {(t2, g2)} is {distance:.2f} km")
