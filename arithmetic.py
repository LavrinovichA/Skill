while True:
    x = float(input('Введите число 1 \n'))
    y = float(input('Введите число 2 \n'))
    z = input('Введите действие \n')
    c = 0
    if z== '+':
        c=x+y
        print(c)
    elif z=='-':
        c=x-y
        print(c)
    elif z=='*':
        c=x*y
        print(c)
    elif z=='/':
        c=x/y
        print(c)
    else:
        print('Недопустимая операция!\n')
    z=input('Хотите продолжить? (Y/N)')
    if z=='n' or z == 'N':
        break