"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies (1c), nickels (5c), dimes (10c), quarters (25c), loonies and toonies.
"""

cents_input = int(input("Enter the value of cents: "))

PENNIES = 1
NICKELS = 5
DIMES = 10
QUARTERS = 25
LOONIES = 100
TOONIES = 200

print(f"{cents_input // TOONIES} toonies")
cents_input %= TOONIES

print(f"{cents_input // LOONIES} loonies")
cents_input %= LOONIES

print(f"{cents_input // QUARTERS} quarters")
cents_input %= QUARTERS

print(f"{cents_input // DIMES} dimes")
cents_input %= DIMES

print(f"{cents_input // NICKELS} nickels")
cents_input %= NICKELS

print(f"{cents_input // PENNIES} pennies")
cents_input %= PENNIES
