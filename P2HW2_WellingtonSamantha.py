#Samantha Wellington
#03/29/2025
#P2HW2
#Define the lowest, highest, sum, and average of users grades

#collect 6 user grades as separate inputs
#store grades in a list
#define lowest grade
#define highest grade
#define sum of grades
#define average
#display lowest, highest, sum, and average



m1 = float(input('Enter grade for Module 1: '))
m2 = float(input('Enter grade for Module 2: '))
m3 = float(input('Enter grade for Module 3: '))
m4 = float(input('Enter grade for Module 4: '))
m5 = float(input('Enter grade for Module 5: '))
m6 = float(input('Enter grade for Module 6: '))

gradesInput = [m1, m2, m3, m4, m5, m6]

lowest = min(gradesInput)

highest = max(gradesInput)

summation = sum(gradesInput)

average = sum(gradesInput)/6


print('\n----------Results----------')
print(f'{'Lowest Grade:':20}', lowest)
print(f'{'Highest Grade:':20}', highest)
print(f'{'Sum of Grades:':20}', summation)
print(f'{'Average:':20}', f'{average:.2f}')
print('----------------------------')
