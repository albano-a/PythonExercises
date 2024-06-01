"""
When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the fol-
lowing formula for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used for temperatures in
degrees Fahrenheit and wind speeds in miles per hour.
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
"""

air_temp = float(input("Enter the air temperature: "))  # 10 degrees max
wind_speed = float(input("Enter the wind speed: "))

WCI = (
    13.12
    + 0.6215 * air_temp
    - 11.37 * wind_speed**0.16
    + 0.3965 * air_temp * wind_speed**0.16
)

print(f"Wind Chill Index: {WCI}")
