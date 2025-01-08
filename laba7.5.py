#Проверка на палиндромы
# Описание: Дан список строк. Нужно отфильтровать строки, которые являются палиндромами (читаются одинаково в обе стороны).
# Используйте функцию filter() и лямбда-выражение, которое проверяет, является ли строка палиндромом.
# Ожидаемый результат: ["level", "radar", "madam"]

words = ["level", "world", "radar", "python", "madam"]

evens = list(filter(lambda x: x == x[::-1], words))
print(evens)  