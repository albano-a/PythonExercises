"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = ( n ) * ( n + 1 ) / 2
"""

number: int = int(input("Enter a number: "))

sum_of_integers = (number) * (number + 1) / 2

print(f"The sum of all integers leading up to {number} is {sum_of_integers}")
