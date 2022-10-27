from ast import While
import os
import math
def square(str):
    P = str * 4
    S = str ** 2
    D = math.sqrt(str ** 2 + str ** 2)
    return(P, S, D)
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
while True:
    while True: # Проверка введенного на соответствие формату числа
        os.system('cls')
        x = (input('Введите сторону квадрата (мм) \n'))
        if is_number(x) == True:
            flag = 0
            x = float(x)
        else:
            os.system('cls')
            print('Не понимаю этого значения\n')
            flag = 1
        if flag == 0:
            break
    print(' Периметр квадрата ', square(x)[0], 'мм\n','Площадь квадрата ',square(x)[1], 'мм^2\n' ,'Диагональ квадрата' ,square(x)[2], 'мм\n') #, 'Площади квадрата 'square[1], 'Диагональ квадрата 'square[2])
    while True: # Проверка введенного на соответствие вопросу
        y=input('Посчитать еще? (Y/N)\n')
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