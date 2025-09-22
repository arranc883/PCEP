condition =  int(input('please tell me your condition:\n 1 = critical\n 2 = serious\n 3 = stable\n  '))

age= int(input('please tell me you age: '))

if condition == 1:
    if age < 12 or age >= 65:
        print('priority highest')
    else:
        print('Age does not match critical condition range.')
    

    
if condition == 2:
    if age > 12 and age < 65:
        print('priority medium')
    else:
        print('Age does not match serious condition range.')


if condition == 3:
    if age >=18 and age < 65:
        print('priority low')
    else:
        print('Age does not match stable condition range.')

