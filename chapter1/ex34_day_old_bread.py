"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. Each of
these amounts should be displayed on its own line with an appropriate label. All of
the values should be displayed using two decimal places, and the decimal points in
all of the numbers should be aligned when reasonable values are entered by the user.
"""

loaves = int(input("How many loaves of day old bread?: "))

PRICE_BREAD = 3.49
PRICE_DAY_OLD = 3.49 * 0.40
total = loaves * PRICE_DAY_OLD  # day old loaves

print("##########################################")
print(f"   Regular price: ${PRICE_BREAD:.2f}")
print(f"Discounted price: ${PRICE_DAY_OLD:.2f}")
print(f"     Total price: ${total:.2f}")
print("##########################################")
