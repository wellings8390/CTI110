# Samantha Wellington
# 04/28/2025
#P4HW2
#create an employee pay calculator that collects multiple employee data
#displays total payment data at the end

#Initiate pay arrays and employee count
otTotal = []
regTotal = []
grossTotal = []
count = 0

#Initiate name and while loop condition
name = input("Enter employee's name or 'Done' to terminate: ")

while name != "Done":
    #increase employee count
    count += 1

    #collect hours worked and rate
    hours = float(input("Enter number of hours worked: "))
    rate = float(input("Enter employee's pay rate: "))

    #Calculate employee pay including overtime pay
    if hours > 40:
        otHours = hours - 40
        otRate = rate * 1.5
        otPay = otRate * otHours
        regPay = 40 * rate
        gross = regPay + otPay

        #store overtime, regular, and gross payments in an array
        otTotal.append(otPay)
        regTotal.append(regPay)
        grossTotal.append(gross)

    else:
        otHours = 0
        otPay = 0
        regPay = hours * rate
        gross = regPay

        #store overtime, regular, and gross payments in an array
        regTotal.append(regPay)
        grossTotal.append(gross)

    #display employee name, pay rate, number of hours worked,
    #overtime hours, overtime pay, regular pay, gross pay
    print ('---------------------------------------------')
    print(f'Employee name: {name} \n')
    print(f'{'Hours Worked':17}{'Pay Rate':12}{'OverTime':12}{'OverTime Pay':16}{'RegHour Pay':16}{'Gross Pay':12}')
    print('-------------------------------------------------------------------------------------------')
    print(f'{hours:<17}{rate:<12}{otHours:<11} ${otPay:<14.2f} ${regPay:<14.2f} ${gross:.2f}')

    name = input("\nEnter employee's name or 'Done' to terminate: ")

    #Once "done", print count and total payments for all employees
    if name == "Done":
        print(f'\nTotal number of employees entered: {count}')
        print(f'Total amount paid for overtime: ${sum(otTotal)}')
        print(f'Total amount paid for regular hours: ${sum(regTotal):.2f}')
        print(f'Total amount paid in gross: ${sum(grossTotal)}')
