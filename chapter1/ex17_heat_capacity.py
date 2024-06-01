"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material's specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:

q = mCΔT

Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.
Extend your program so that it also computes the cost of heating the water. 
Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
your program to compute the cost of boiling the water needed for a cup of coffee.
"""

WATER = 1000  # grams
DELTA_T = 80  # celsius
HEAT = 4.186

ENERGY = WATER * DELTA_T * HEAT  # result in joules
COST = ENERGY * 2.778e-7 * 0.089

print(f"The amount of energy needed to heat up {WATER} grams of water")
print(f"by {DELTA_T} degrees is equal to {ENERGY} J")
print()
print(f"The total cost is {COST} dollars")
