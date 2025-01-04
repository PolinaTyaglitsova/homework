#Дана строка, состоящая из символов. Необходимо подсчитать частоту каждого символа в строке и вывести ее
# Вывод: {'a' : 5, 'b' : 2, 'r' : 2,  'c' : 1, 'd' : 1}

string = "abracadabra"

string_new = {}
for i in string:
    if i in string_new:
        string_new[i] = string_new[i] + 1
    else:
        string_new[i] = 1

print(string_new)