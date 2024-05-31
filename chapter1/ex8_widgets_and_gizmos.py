"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts.
"""

widgets = float(input("Enter the number of widgets: "))
gizmos = float(input("Enter the number of gizmos: "))

total_weight = ((widgets * 75) + (gizmos * 112)) * 0.001

print(f"The total weight is {total_weight}Kg")
