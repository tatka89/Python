a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
res = 0
x = 0
while x!=abs(b):
    res = res + abs(a)
    x +=1
print(res) if a*b>=0 else print('-' + str(res))
