"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

TIP = 0.18
TAX = 0.12

value_meal = float(input("Enter the cost of the meal you ordered at Olive Garden: "))

total_amount = value_meal + (TIP * value_meal) + (TAX * value_meal)

print(f"Amount of tax: ${(TAX*value_meal):.2f}")
print(f"Amount of tip: ${(TIP*value_meal):.2f}")
print(f"Total cost: ${total_amount:.2f}")
