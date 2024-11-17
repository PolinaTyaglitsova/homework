#  Ввести целое число и определить, верно ли, что все его цифры расположены в порядке возрастания
a = int(input("Введите число "))
metka = True
last_digit = a % 10
while a > 0:
    if last_digit < a % 10:
       metka = False
    last_digit = a % 10
    a = a // 10 
if metka == True:
    print("В порядке возрастания")
else:
    print("Не в порядке возрастания")