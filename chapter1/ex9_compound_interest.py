"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
"""

initial_amount = float(input("Enter the amount of money deposited in the beginning: "))

one_year = initial_amount + (4 / 100) * initial_amount
second_year = one_year + (4 / 100) * one_year
third_year = second_year + (4 / 100) * second_year

print(f"The initial amount in 2024 was: ${initial_amount:.2f}")
print(f"The amount in the year 2025 is ${one_year:.2f}")
print(f"The amount in the year 2026 is ${second_year:.2f}")
print(f"The amount in the year 2027 is ${third_year:.2f}")
