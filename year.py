while True:
    y = int(input('Введите год \n'))
    if y % 4 == 0:
        print('Год високосный\n')
    else:
        print('Не високосный год\n')
    while True:
        y=input('Хотите продолжить? (Y/N)\n')
        if y=='n' or y == 'N':
            flag = 0
            break
        elif y == 'y' or y == 'Y':
            flag = 1 
            break
        else:
            print('Не корректное значение\n')
    if flag == 0:
        break