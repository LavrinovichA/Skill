import os
def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
while True:
    os.system('cls')
    while True:
        y = (input('Введите год для проверки \n'))
        if is_number(y) == True :
            flag = 0
            year = int(y)
        else:
            os.system('cls')
            print('Год пишется иначе\n')
            flag = 1
        if flag == 0:
            break
    if year % 4 == 0:
        print('Год високосный\n')
    else:
        print('Год не високосный\n')
    while True:
        y=input('Хотите проверить еще один год? (Y/N)\n')
        if y=='n' or y == 'N':
            flag = 0
            break
        elif y == 'y' or y == 'Y':
            flag = 1 
            break
        else:
            os.system('cls')
            print('Определитесь уже! ДА (Y) или НЕТ (N)\n')
    if flag == 0:
        break