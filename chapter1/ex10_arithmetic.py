"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a 
"""

import math

A = float(input("Enter a value for a: "))
B = float(input("Enter a value for b: "))

the_sum = A + B
the_dif = A - B
the_prod = A * B
the_quo = A / B
the_rem = A % B
the_log = math.log10(A)
the_pow = A**B

print(f"Sum: {the_sum:.2f}")
print(f"Dif: {the_dif:.2f}")
print(f"Prod: {the_prod:.2f}")
print(f"Quo: {the_quo:.2f}")
print(f"Rem: {the_rem:.2f}")
print(f"Log: {the_log:.2f}")
print(f"Pow: {the_pow:.2f}")
