# Написать программу, которая предлагает пользователю ввести номер дня недели,
# и в ответ показывает название этого дня (например, 6 – это суббота).
# Решить с использованием if и switch.

n = int(input('Введите номер дня недели: '))

match n: 
  case 1: print("Понедельник")
  case 2: print("Вторник")
  case 3: print("Среда")
  case 4: print("Четверг")
  case 5: print("Пятница")
  case 6: print("Суббота")
  case 7: print("Воскресенье")

