a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

mySum = a+b+c
myProizved = a*b*c
myAverage = (a+b+c)/3

print('Сумма чисел: ' + str(mySum) ,
       'Произведение чисел: ' + str(myProizved) ,
       'Среднее арифметическое чисел: ' + str (myAverage), sep='\n')