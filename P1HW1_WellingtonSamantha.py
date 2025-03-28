#Samantha Wellington
#03/25/2025
#P1HW1
#Execute math operations using user input variables

#exponential operations
print('\n -----Caluclating Exponenets-----\n')
base = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent: '))
value1 = base ** exponent
print('\n\n', base, 'raised to the power of', exponent, 'is', value1, '!!')

#add/subtract operations
print('\n -----Addition and Subtraction-----\n')
start = int(input('Enter a starting integer: '))
add = int(input('Enter an integer to add: '))
subtract = int(input('Enter an integer to subtract: '))
value2 = start + add - subtract
print('\n\n', start, '+', add, '-', subtract, 'is equal to', value2)