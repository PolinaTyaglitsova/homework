#Задание 1: Возведение чисел в квадрат
#Описание: Дан список целых чисел. Необходимо создать новый список, в котором каждое число из исходного списка возведено в квадрат.
#Ожидаемый результат: [1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]
squared= list(map(lambda x: x ** 2, numbers))
print(squared)