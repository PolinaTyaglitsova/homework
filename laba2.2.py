a = int(input("Введите число а "))
b = int(input("Введите число b "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)