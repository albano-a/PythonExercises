"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the Internet.
"""

celsius = float(input("Temperature in Celsius: "))
fah = celsius * (9 / 5) + 32
kel = celsius + 273.15

print(f"The temperature in Celsius is: {celsius}ºC")
print(f"The temperature in Fahrenheit is: {fah}ºF")
print(f"The temperature in Kelvin is: {kel}ºK")
