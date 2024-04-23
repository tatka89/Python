from math import sqrt

x1 = float(input('Введите x1 координату точки A: '))
y1 = float(input('Введите y1 координату точки A: '))
x2 = float(input('Введите x2 координату точки B: '))
y2 = float(input('Введите y2 координату точки B: '))

LenAB = sqrt((x2-x1)**2+(y2-y1)**2)

print('Длина отрезка AB = ' + str(LenAB))