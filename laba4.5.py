#Даны две строки. Необходимо определить являются ли она анаграммами (содержат одинаковые символы с одинаковой частотой)
# Вывод: True
string1 = "listen"
string2 = "silent"
result = set(string1) == set(string2)

if result:
    print(True)
else:
    print(False)