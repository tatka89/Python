s = float(input('Введите расстояние марафонца: '))*1000
v = float(input('Введите скорость марафонца: '))

t = s/v
#print('Марафонец пробежал за {} часов {} минут {} секунд'.format('%d' % (t//3600), '%d' %(t%3600//60), '%d' %(t%60)))
print('%d' % (t//3600) + ' ч. ' + '%d' %(t%3600//60) + ' мин. '+ '%d' %(t%60) +' сек.' )