# 2.	Ввести три числа и найти наименьшее среди них.

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

'1 способ'
#print(min(a,b,c))

'2 способ'
myMin = a 

if b < myMin:
    myMin = b
if c < myMin:
    myMin = c

print('Минимально число: ',myMin)