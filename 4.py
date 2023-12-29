# Возведение числа x в степень y

def power(number, pow):
    if pow == 0:
        return 1
    return number * power(number, pow - 1)

print(power(2, 10))