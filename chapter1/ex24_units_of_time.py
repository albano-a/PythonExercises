"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""

days, hours, minutes, seconds = input(
    "Enter the duration (days, hours, minutes, seconds): "
).split(",")

days2seconds = int(days) * 24 * 60 * 60
hours2seconds = int(hours) * 60 * 60
minutes2seconds = int(minutes) * 60

total = int(seconds) + minutes2seconds + hours2seconds + days2seconds

print(
    f"The duration {days} days, {hours}h, {minutes}min, {seconds}s is equal to {total} seconds"
)
