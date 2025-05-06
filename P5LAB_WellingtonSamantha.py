# Samantha Wellington
# 05/04/2025
#P5LAB
#Generate a random amount owed by a customer. Use functions to take in how much the customer will pay with and provide the change.

import random

def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${owed:.2f}')

    pay = float(input('How much cash will you put in the self-checkout? $'))

    while pay < owed:
        print(f'\nYou must pay with an amount greater than or equal to ${owed}.')
        pay = float(input('How much cash will you put in the self-checkout? $'))

    change = round(pay - owed, 2)

    print(f'Change is: ${change:.2f}\n')

    disperse_change(change)

def disperse_change(total):

    #print no change if total is 0 or less
    if(total) <= 0:
        print('No Change')

    #calculate denominations if money greater than zero
    else:
        intTotal = int(total*100)
        dollars = intTotal // 100
        rem = intTotal - dollars*100
        quarters = rem // 25
        rem = rem - 25*quarters
        dimes = rem // 10
        rem = rem - 10*dimes
        nickels = rem // 5
        rem = rem - 5*nickels
        pennies = rem // 1

        #display change
        #dollars
        if dollars == 1:
            print(f'{dollars} Dollar')
        if dollars > 1:
            print(f'{dollars} Dollars')

        #quarters
        if quarters == 1:
            print(f'{quarters} Quarter')

        if quarters > 1:
            print(f'{quarters} Quarters')

        #dimes
        if dimes == 1:
            print(f'{dimes} Dime')

        if dimes > 1:
            print(f'{dimes} Dimes')

        #nickels
        if nickels == 1:
            print(f'{nickels} Nickel')

        if nickels > 1:
            print(f'{nickels} Nickels')

        #pennies
        if pennies == 1:
            print(f'{pennies} Penny')

        if pennies > 1:
            print(f'{pennies} Pennies')

main()