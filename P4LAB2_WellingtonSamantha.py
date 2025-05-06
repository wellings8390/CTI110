# Samantha Wellington
# 04/27/2025
#P4LAB2
#This program takes a user input integer and displays a multiplication table.

test = "yes"

while test == "yes":
    number = int(input("\nEnter an integer: "))

    if number < 0:
        print("\nThis program does not accept negative numbers.")

    elif number > -1:
        for x in range(1,13):
            print(f'{number} * {x} = {number*x}')

    test = str(input("\nWould you like to run the program again? (yes or no): "))

    if test == "no":
        print("\nExiting program...")



