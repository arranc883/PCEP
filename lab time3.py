age=int(input('please enter how old you are: '))

distance=int(input('please enter the distance you are travelling: '))

if distance<1000:
    if age<12:
        print('your price is $200')

    elif age<64:
        print('your price is $300')

    elif age>=65:
        print('your price is $250')

elif distance>1000:
    if age<12:
        print('your price is $400')

    elif age<64:
        print('your price is $500')

    elif age>=65:
        print('your price is $450')