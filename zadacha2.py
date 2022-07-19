# задача 2 урок 1
num = int(input())  # переменная которую вводит пользовательно в секундах
minuts = num // 60
sek = (num % 60)
chas = minuts // 60
minut1 = minuts % 60
if chas<10: # если часы меньше 10, будет выводиться некрасиво, надо чтобы тогда был 0 перед цифрой
    chas = str(chas)
    chas = ('0'+chas)
else:
    chas = str(chas)
if minut1 < 10:
    minut1 = str(minut1)
    minut1 = ('0'+minut1)
else:
    minut1 = str(minut1)
if sek < 10:
    sek = str(sek)
    sek = ('0'+sek)
else:
    print(chas, minut1, sek, sep=':')





