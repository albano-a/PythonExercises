"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:

If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula:
"""

height, weight = input("Enter your height and weight: ").split(",")

# Now, calculates the bmi
BMI = float(weight) / (float(height) ** 2)

print(f"The value of BMI is {BMI:.2f} for the weight {weight}kg and height {height}m")
