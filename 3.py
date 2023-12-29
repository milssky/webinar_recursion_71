# Реверсирование числа. Использование строк запрещено!
# 1234 -> 4321 = 4000 + 300 + 20 + 1
# 1. Посчитать количество цифр
# 2. Умножить последнюю цифру на 10 в степени количество - 1
# 3. Сложить п.2 для остальный разрядов

def recursive_reverse_number(number: int) -> int:
    if number == 0:
        return 0

    count_digits = 0

    number_copy = number
    while number_copy > 0:
        count_digits += 1
        number_copy //= 10  # number = number // 10
    
    last_digit = number % 10
    result = last_digit * 10**(count_digits - 1)
    return result + recursive_reverse_number(number // 10)

print(recursive_reverse_number(12345678))