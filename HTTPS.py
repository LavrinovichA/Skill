import os

while True:
    sayt=input('Введите адре сайта \n')
    if sayt=='завершить':
        break

    if 'https://'in sayt:
        os.system('start ' + sayt)
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.sistem('start ' + sayt)
    else:
        sayt ='https://www.' + sayt
        os.system('start ' + sayt)