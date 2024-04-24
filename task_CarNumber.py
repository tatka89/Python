import re

S = "Авто номер E100EE22RUS, следующий номер A618PD293RUS"

res = re.findall(r'[A-Z]\d{3}[A-Z]{2}\d{2,3}RUS',S)

print(res)