#Ввести два целых числа a и b (a ≤ b) и вывести квадраты всех чисел от a до b. Формат входных данных: 
#Два целых числа по модулю не больше 100 Формат результата: Квадраты чисел от a до b.
a = int(input("Введите число а "))
b = int(input("Введите число b "))

if a <= b and (a + b) <= 100:
    for i in range(a, b+1):
        print(i**2) 