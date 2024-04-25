
# получим объект файла
file1=open("sample.txt","r", encoding='utf-8')

while True:
    #считываем строку
    line=file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip())

# закрываем файл
file1.close