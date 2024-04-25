#my_file=open("myFile.txt","a+")
#my_file.write("Добавляем новый текст")
#my_file.close()

my_file=open("myFile.txt","r")
file_contents=my_file.read()
print(file_contents)
