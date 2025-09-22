heath = input('have you paid for health insurance? ')
charity = input('have you made charitable donations? ')
income = int(input('what is you income? '))

if income <= 10_000:
    tax = 0

elif income > 10_000 and income <= 50_000:
    tax = income * 0.1

elif income > 50_000:
    tax = income * 0.2
else:
    print('error')

if heath.lower().strip() == 'yes':
    tax -= tax * 0.05

if charity.lower().strip() == 'yes':
    tax -= tax *0.1


print(f'your tax is {tax}')


