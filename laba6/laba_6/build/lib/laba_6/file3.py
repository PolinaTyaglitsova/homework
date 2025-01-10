def summ_eq_mult(a):
    sum = 0
    mlt = 1
    for i in range(1, len(str(a)) + 1):
        last_digit = a % 10
        sum = sum + last_digit
        mlt = mlt * last_digit
        a = a // 10
    if sum == mlt:
        return "Сумма цифр равна произведению цифр"
    return "Сумма цифр не равна произведению цифр"
