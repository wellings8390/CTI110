#Samantha Wellington
#04/27/2025
#P4HW1
#Define the lowest, highest, sum, and average of users grades

#Ask user the number of grades they want to enter
loops = int(input("How many scores do you want to enter?: "))
x = 0
grades = []

#Collect and store the grades using a loop
while x < loops:
    score = float(input(f'Enter score #{x+1}: '))

    # Ensure each score is between 0 and 100, if not, ask for valid score
    if score < 0 or score > 100:
        while not score in range(0,100):
            print("INVALID Score entered!! \n Score should be between 0 and 100")
            score = float(input(f'Enter score #{x+1} again: '))

    grades.append(score)
    x += 1

#Display lowest score, score list (dropping lowest),
#Average score of modified list, and letter grade

low = min(grades)
grades.remove(low)
high = max(grades)
add = sum(grades)
avg = add/len(grades)

#Determine letter grade
if avg >= 90:
    letter = "A"

if 80 <= avg < 90:
    letter = "B"

if 70 <= avg < 80:
    letter = "C"

if 60 <= avg < 70:
    letter = "D"

if avg < 60:
    letter = "F"

#print low, modified, average, and letter

print('\n----------Results----------')
print(f'{'Lowest Score':15}{":":2}', low)
print(f'{'Modified List':15}{":":2}', grades)
print(f'{'Average':15}{":":2}', f'{avg:.2f}')
print(f'{'Grade':15}{":":2}', letter)
print('----------------------------')



