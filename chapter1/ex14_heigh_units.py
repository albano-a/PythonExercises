"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
"""

feet, inches = input("Enter a height in feet inch: ").split(" ")

centimeters = 2.54 * (12 * float(feet) + float(inches))

print(f"The value {feet}'{inches} is equivalent to {centimeters} cm")
