"""
Write a program that asks the user to enter the width and length of a room. Once
these values have been read, your program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

user_input = input("Enter the width and length of the room in meters: ")
width, height = user_input.split(",")

area: float = float(width) * float(height)

print(f"The area of the room is {area} square meters")
