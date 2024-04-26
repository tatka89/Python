#3.	Вычислить сумму чисел в диапазоне от M до N. 

M = int(input('Ведите натуральное число: '))
N = int(input('Ведите натуральное число: '))
sum_MN=N
for i in range(M,N):
    sum_MN = sum_MN+i
   
print(sum_MN)        