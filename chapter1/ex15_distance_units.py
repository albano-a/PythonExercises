"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don't have them memorized.
"""

feet_val = float(input("Enter a measurement in feet: "))

feet2inches = feet_val * 12
feet2yards = feet_val / 3
feet2miles = feet_val / 5280

print(
    f"{feet_val}ft is equal to {feet2inches:.2f} inches, {feet2yards:.2f} yards, and {feet2miles:.2f} miles"
)
