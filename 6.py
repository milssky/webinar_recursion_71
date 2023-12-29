# Перевод из десятичной системами исчисления в двоичную
# 16 -> 10000


def recusion_dec_to_bin(number:int, k:int = 0) -> int:
    if number == 0:
        return 0
    d = number % 2
    return d * 10**k + recusion_dec_to_bin(number // 2, k+1)

print(recusion_dec_to_bin(19))