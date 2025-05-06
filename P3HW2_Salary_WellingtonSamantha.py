# Samantha Wellington
# 04/23/2025
#P3HW2_Salary
#create an employee pay calculator

# input employee name, hours worked, and pay rate
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

#Calculate employee pay including overtime pay
if hours > 40:
    otHours = hours - 40
    otRate = rate * 1.5
    otPay = otRate * otHours
    regPay = 40 * rate
    gross = regPay + otPay

else:
    otHours = 0
    otPay = 0
    regPay = hours * rate
    gross = regPay

#display employee name, pay rate, number of hours worked,
#overtime hours, overtime pay, regular pay, gross pay

print ('---------------------------------------------')
print(f'Employee name: {name} \n')
print(f'{'Hours Worked':17}{'Pay Rate':12}{'OverTime':12}{'OverTime Pay':16}{'RegHour Pay':16}{'Gross Pay':12}')
print('-------------------------------------------------------------------------------------------')
print(f'{hours:<17}{rate:<12}{otHours:<11} ${otPay:<14.2f} ${regPay:<14.2f} ${gross:.2f}')
