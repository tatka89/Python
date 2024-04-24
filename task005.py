a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

M = a
if b > M:
    M=b
if c > M:
    M=c
print('Максимальное число ' + str(M))