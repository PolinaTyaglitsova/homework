#Дан список чисел. Требуется выполнить циклический сдвиг на заданное число позиций. 
# Элементы, смещаемые за пределы массива, должны переходить в начало
import copy

my_list = [1,2,3,4,5]
shift = 3

for i in range(shift):
    result = copy.deepcopy(my_list)
    result.insert(0, my_list[-1])
    result.pop(-1)
    my_list = result

print(result)