"""
Write a program that implements the Anonymous Gregorian Computus algorithm
to compute the date of Easter. Your program should read the year from the user and
then display a appropriate message that includes the date of Easter in that year.
"""

from math import floor


YEAR = 2000

a = YEAR % 19
b = floor(YEAR / 100)
c = YEAR % 100
d = floor(b / 4)
e = b % 4
f = floor((b + 8) / 25)
g = floor((b - f + 1) / 3)
h = (19 * a + b - d - g + 15) % 30
i = floor(c / 4)
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = floor((a + 11 * h + 22 * l) / 451)
month = floor((h + l - 7 * m + 114) / 31)
day = 1 + ((h + l - 7 * m + 114) % 31)

print(f"Easter in the year {YEAR} is on {day}/{month} ")
