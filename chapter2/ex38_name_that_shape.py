"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

num_sides = int(input("Enter the number of sides: "))

if num_sides == 3:
    print(f"A shape with {num_sides} sides is a triangle")
elif num_sides == 4:
    print(f"A shape with {num_sides} sides is a square")
elif num_sides == 5:
    print(f"A shape with {num_sides} sides is a pentagon")
elif num_sides == 6:
    print(f"A shape with {num_sides} sides is a hexagon")
elif num_sides == 7:
    print(f"A shape with {num_sides} sides is a heptagon")
elif num_sides == 8:
    print(f"A shape with {num_sides} sides is a octagon")
elif num_sides == 9:
    print(f"A shape with {num_sides} sides is a nonagon")
elif num_sides == 10:
    print(f"A shape with {num_sides} sides is a decagon")
