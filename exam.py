# Считать массив из 12 элементов и выполнить инверсию для каждой трети массива.
# Формат входных данных: 12 целых чисел через пробел
# Формат результата: 12 целых чисел через пробел
#Примеры
#Входные данные
#4 -5 3 10 -4 -6 8 -10 1 0 5 7
#Результат работы
#10 3 -5 4 -10 8 -6 -4 7 5 0 1
# Считываем входные данные

input_data = input("Введите 12 целых чисел через пробел: ")
array = list(map(int, input_data.split()))

if len(array) != 12:
    print("Ошибка: необходимо ввести ровно 12 чисел.")
else:
    part1 = array[0:4]
    part2 = array[4:8]
    part3 = array[8:12]

    inverted_part1 = part1[::-1]
    inverted_part2 = part2[::-1]
    inverted_part3 = part3[::-1]

    result_array = inverted_part1 + inverted_part2 + inverted_part3

    print("Результат работы:")
    print(" ".join(map(str, result_array)))

