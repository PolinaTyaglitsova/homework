#Произведение всех чисел в списке
#Описание: Дан список чисел. Необходимо вычислить произведение всех чисел в списке, используя лямбда-выражение.
#Используйте функцию reduce() из модуля functools и лямбда-выражение для получения произведения всех чисел.
#Ожидаемый результат: 24

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product) 