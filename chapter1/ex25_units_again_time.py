"""
In this exercise you will reverse the process described in Exercise 24. Develop a
program that begins by reading a number of seconds from the user. Then your program
should display the equivalent amount of time in the form D:HH:MM:SS, where D,
HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours,
minutes and seconds should all be formatted so that they occupy exactly two digits.
Use your research skills determine what additional character needs to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.
"""

seconds = int(input("Enter the number of seconds: "))
MIN = 60  # Seconds in a minute
HOUR = 3600  # Seconds in an hour
DAYS = 84600  # Seconds in a day

_days_ = seconds // DAYS
print(f"{_days_:02} days")
seconds %= DAYS

_hours_ = seconds // HOUR
print(f"{_hours_:02} hours")
seconds %= HOUR

_mins_ = seconds // MIN
print(f"{_mins_:02} minutes")
seconds %= MIN

_seconds_ = seconds
print(f"{_seconds_:02} seconds")

print(f"{_days_:02}:{_hours_:02}:{_mins_:02}:{_seconds_:02}")
