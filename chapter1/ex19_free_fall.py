"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s².
"""

from math import sqrt

d_height: float = float(
    input("Enter the height from which the object is dropped in meters (m): ")
)

vel_f = sqrt(0**2 + 2 * 9.8 * d_height)

print(f"The final velocity of a object dropped from {d_height}m is {vel_f:.2f}m/s")
