#Дан список чисел и размер блока. Нужно развернуть элементы в каждом блоке по отдельности. 
# Если последний блок меньше по размеру то его нужно оставить без изменений  [3,2,1,6,5,4,7]
array = [1,2,3,4,5,6,7]
array_1 = []
spisok = []
n = 3
s = (len(array)) % n
for i in range((len(array))//n):
    array_1 = array[:n]
    array_1.reverse()
    array = array[3:]
    spisok.append(array_1)
if (len(array)) % n == 0:
    print(sum(spisok, []))
else:
    spisok. append(array[-s:])
    print(sum(spisok, []))



