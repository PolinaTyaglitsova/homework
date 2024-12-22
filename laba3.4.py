#Дан список целых чисел и длина подмассива k. Нужно найти подмассив длины k, сумма элементов которого будет максимальной
import copy

my_list = [1, -2, 3, 4, -1, 2, 1, -5, 4]
result = copy.deepcopy(my_list)
k = 3
max_0 = 0

def proverka(max_0):
   for i in range(k):
     max = max_0 + int(result[i])
if max > max_0:
   max_0 == max

for j in range(len(my_list)):
   print(proverka(max_0))
   result.pop(0)

print(max_0)