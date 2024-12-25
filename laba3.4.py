#Дан список целых чисел и длина подмассива k. Нужно найти подмассив длины k, сумма элементов которого будет максимальной

my_list = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3
max_0 = 0

def proverka(my_list,k):
   max_0  = sum(my_list[:k])
   max1 = max_0

   for i in range(k,len(my_list)):
     max1 = max1 + my_list[i] - my_list[i-k]
     max_0 = max(max_0 ,max1)

   return max_0

result = proverka(my_list,k)
print(result)
