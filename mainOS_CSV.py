import csv
myFile=open('myFile.csv',encoding='UTF-8')
exampleReader=csv.reader(myFile,delimiter=';')
exampleData=list(exampleReader)
print(exampleData)
myFile.close()


