from functools import reduce #подключаем функцию reduce()
numbers = [1,2,3,4,5]
mult = reduce(lambda x,y: x*y, numbers)
print(mult)