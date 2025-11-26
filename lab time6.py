def add(num1 ,num2):
    answer = num1 + num2
    print(answer)

def subtract(num1 ,num2):
    answer = num1 - num2
    print(answer)

def muliply(num1 ,num2):
    answer = num1 * num2
    print(answer)

def divide(num1 ,num2):
    answer = num1 / num2
    print(answer)

def main():
    a = input('Would you like to: add, subtract, multiply, divide - ').strip().lower()

    x = int(input(f'What number would you like to {a} first - '))
    y = int(input(f'What number would you like to {a} second - '))

    if a=='add':
        add(x,y)

    elif a=='subtract':
        subtract(x,y)

    elif a=='muliply':
        muliply(x,y)

    elif a=='divide':
        divide(x,y)

    else:
        print('There has been a mistake please try again.')
        main()

main()