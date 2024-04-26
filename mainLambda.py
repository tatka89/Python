number = lambda num: num*2
print(number(8))

numbs = ['4', '23', '15', '8']
max_str = max(numbs, key = lambda num:int(num))
print(max_str)

int_numbs = list(map (int, numbs))
print(int_numbs)

base = [1,2,5,6]
exp = [2,3,4,5]

data = list(map(lambda x,y: x**y, base, exp))
print(data)

words = ['красный','синий','оранжевый','белый']
long_words = list(filter(lambda line: len(line) > 5, words))
print(long_words)