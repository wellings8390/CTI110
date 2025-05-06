# Samantha Wellington
# 04/22/2025
# P3HW1
# This program takes 6 grades, and determines the lowest, highest, sum, and average grade. Then displays the grade letter.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
add = sum(grades)
avg = add/len(grades)

#print high, low, sum, and average grades

print('\n----------Results----------')
print(f'{'Lowest Grade:':20}', low)
print(f'{'Highest Grade:':20}', high)
print(f'{'Sum of Grades:':20}', add)
print(f'{'Average:':20}', f'{avg:.2f}')
print('----------------------------')

# determine letter grade for average

if avg >= 90:
 print('Your grade is: A')

if 80 <= avg < 90:
 print('Your grade is: B')

if 70 <= avg < 80:
 print('Your grade is: C')

if 60 <= avg < 70:
 print('Your grade is: D')

if avg < 60:
 print('Your grade is: F') # TO DO: finish this





