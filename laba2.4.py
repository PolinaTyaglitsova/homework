a = int(input())

def summ_digit(a):
    sum = 0
    for i in range(1, len(str(a))+1):
        last_digit = a % 10
        sum = sum + last_digit
        a = a // 10
    return sum

print(summ_digit(a))