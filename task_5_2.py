#Проверить, имеет ли введённое число вещественную часть.
# Например, числа 3.14 и 2.5 – имеют вещественную часть, а числа 5 и 10.0 – нет.

x = float(input('Введите вещественное число: '))

if x%1 == 0:
    print('Введенное число не имеет вещественную часть')
else:
    print('Введенное число имеет вещественную часть')