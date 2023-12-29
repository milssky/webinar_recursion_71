# Вычислить количество отрицательных чисел в наборе
# [1, -1, -1000, 2, 3] -> 2


def recursion_count_negative_numbers(numbers: list[int]) -> int:
    if numbers == []:
        return 0
    return (numbers[0] < 0) + recursion_count_negative_numbers(numbers[1:])



numbers = [1, -1, -1000, 2, 3]
print(recursion_count_negative_numbers(numbers))
