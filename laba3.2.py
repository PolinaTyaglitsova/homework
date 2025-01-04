#Дан вложенный список, состоящий из нескольких списков одинаковой длины. 
# Нужно выполнить циклический сдвиг элементов внутри каждого из вложенных списков 
# [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shift = 1

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shift = 1

def matrix_sdvig(matrix, shift):
    new_list = []
    for result in matrix:
        shifted_result = result[-shift:] + result[:-shift]
        new_list.append(shifted_result)
    return new_list

result = matrix_sdvig(matrix, shift)
print(result)