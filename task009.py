import random

rand_list = []
rand_list_2 = []
N = 10

for i in range(N):
    rand_list.append(random.randint(-10,10))
    if rand_list[i] % 2 == 0 and rand_list[i] < 0:
        rand_list_2.append(rand_list[i])

print (rand_list)
print (rand_list_2)