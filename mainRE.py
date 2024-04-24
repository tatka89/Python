import re
fio = "Иванов Иван Иванович"
result = re.match(r'Иван',fio)
print(result.string)
print(result.group(0))
print(result.end(0))
print(result.endpos)

result = re.fullmatch(r'Иван',fio)
print(result)

result = re.findall(r'Иван',fio)
print(result)

result = re.split(r' ',fio)
print(result)

result=re.sub(r'Иван','Петр',fio)
print(result)

pattern=re.compile('Иван')
result=pattern.findall(fio)
print(result)

res=re.findall(r'.',fio)
print(res)

res=re.findall(r'\w',fio)
print(res)

res=re.findall(r'\w*',fio)
print(res)

res=re.findall(r'\w+',fio)
print(res)

res=re.findall(r'^\w+',fio)
print(res)

res=re.findall(r'\w+$',fio)
print(res)

res=re.findall(r'\w\w',fio)
print(res)

res=re.findall(r'\b\w',fio)
print(res)