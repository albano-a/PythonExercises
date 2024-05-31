"""
Create a program that reads the length and width of a farmer's field from the user in
feet. Display the area of the field in acres.
"""

user_input = input("Enter the width and length of the room in feet: ")
width, height = user_input.split(",")

area_feet: float = float(width) * float(height)
area_acres = area_feet / 43560

print(f"The area of the field is {area_acres:.2f} acres")
