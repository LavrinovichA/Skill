while True:
    y = int(input('Введите год \n'))
    if y % 4 == 0:
        print('Год високосный\n')
    else:
        print('Не високосный год\n')
    y=input('Хотите продолжить? (Y/N)\n')
    if y=='n' or y == 'N':
        break