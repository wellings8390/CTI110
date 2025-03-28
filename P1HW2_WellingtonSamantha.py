# Samantha Wellington  
# 03/25/2025
# P1HW2
# Take user input about the destination and expenses of a trip. Output user travel info and remaining balance


print('\n\n-----Enter Your Travel Information-----\n')
#collect user budget
budget = int(input('Enter budget: '))

#collect user destination
destination = str(input('Enter your travel destination: '))

#collect user gas estimate
gas = int(input('How much do you think you will spend on gas? '))

#collect user hotel cost
hotel = int(input('Approximately, how much will you need for accomodation/hotel? '))

#collect user food cost
food = int(input('Lastly, how much will you need for food? '))

#output user travel info
print('\n\n-----Travel Expenses-----\n')
print('Location: ', destination)
print('Initial Budget: ', budget, '\n')

print('Fuel: ', gas)
print('Accomodation: ', hotel)
print('Food: ', food, '\n')

# calculate expenses from budget
balance = budget-gas-hotel-food

#display remaining balance
print('Remaining Balance: ', balance)

 