#Дана строка. Напишите программу, которая:
#удалит все повторяющиеся подряд символы, оставив только один символ из каждого фрагмента
#выведет получившуюся строку
s = "aaabbbcccaaadddd"
s= set(s)
print(''.join(sorted(s)))