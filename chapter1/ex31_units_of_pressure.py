"""
In this exercise you will create a program that reads a pressure from the user in kilo-
pascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

pressure = float(input("The pressure: "))  # kilo-pascal

psi = pressure / 6.895  # pounds per square inch
mmHg = pressure * 7.50062  # millimeters of mercury
atm = pressure / 101.3  # atmospheres

print("Pressure:")
print(f"{pressure:.2f} kPa")
print(f"{psi:.2f} PSI")
print(f"{mmHg:.2f} mmHg")
print(f"{atm:.2f} atm")
