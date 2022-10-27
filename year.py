def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
while True:
    while True:
        y = (input('Введите год \n'))
        if is_number(y) == True :
            flag = 0
            year = int(y)
        else:
            print('Не корректное значение\n')
            flag = 1
        if flag == 0:
            break
    if year % 4 == 0:
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