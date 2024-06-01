"""
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

sound_level = int(input("Enter a decibel (dB) value: "))

if sound_level > 130:
    print("I am going to be deaf!")
elif sound_level < 40:
    print("I can't hear anything!")
elif 40 < sound_level < 70:
    print("This value of dB is between Quiet Room and Alarm Clock.")
elif 70 < sound_level < 106:
    print("This value of dB is between Alarm Clock and Gas Lawnmower.")
elif 106 < sound_level < 130:
    print("This value of dB is between Gas Lawnmower and Jackhammer.")
elif sound_level == 40:
    print("This value is equivalent to a Quiet Room.")
elif sound_level == 70:
    print("This value is equivalent to a Alarm Clock.")
elif sound_level == 106:
    print("This value is equivalent to a Gas Lawnmower.")
elif sound_level == 130:
    print("This value is equivalent to a Jackhammer.")
else:
    print("Not a valid input")
