# Samantha Wellington
# 04/22/2025
# Module_5
# Calculate the most efficient way to make a specified amount of money

#take user money input
total = float(input('Enter the amount of money as a float: $'))

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
