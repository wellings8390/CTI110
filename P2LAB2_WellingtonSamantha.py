# Samantha Wellington
# 03/27/2025
# P2LAB2
# Create a dictionary of cars and their mpg. Prompt the user to select a car from the dictionary, 
# then enter how many miles they would like to travel. Output how many gallons of gas they will need.

#create and print dictionary 
carMPG = {'Camaro': 18.21,
          'Prius': 52.36,
          'Model S': 110,
          'Silverado': 26}

keys = carMPG.keys()
print('\n\n', keys, '\n')

#user input which car 
travelCar = input('Which car will you be traveling in? This program is case-sensitive. ')

#output car mpg info
print('The', travelCar, 'gets', carMPG.get(travelCar), "miles per gallon.", '\n')

#user input how many miles traveling
miles = int(input('How many miles will you drive the ' + travelCar + '? Enter this number as an integer. '))

#calculate gas needed
mpg = carMPG.get(travelCar)
gas = miles / mpg

#output gas needed
print('You will need', f'{gas:.2f}' + ' gallons of gas to drive the', travelCar, miles, 'miles.')