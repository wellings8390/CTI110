 #Samantha Wellington
 #03/27/2025
 #P2HW1
 #Change and organize the output of P1HW2 



print('\n\n-----Enter Your Travel Information-----\n')
#collect user budget
budget = float(input('Enter your budget: '))

#collect user destination
destination = str(input('\nEnter your travel destination: '))

#collect user gas estimate
gas = float(input('\nHow much do you think you will spend on gas? '))

#collect user hotel cost
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))

#collect user food cost
food = float(input('\nLastly, how much will you need for food? '))

#output user travel info
print('\n\n----------Travel Expenses----------')
print(f'{'Location:':20}', destination)
print(f'{'Initial Budget:':20}', f'${budget:.2f}')
print(f'{'Fuel:':20}', f'${gas:.2f}')
print(f'{'Accomodation:':20}', f'${hotel:.2f}')
print(f'{'Food:':20}', f'${food:.2f}')

# calculate expenses from budget
balance = budget-gas-hotel-food

#display remaining balance
print('------------------------------------\n')
print(f'{'Remaining Balance:':20}', f'${balance:.2f}', '\n')
