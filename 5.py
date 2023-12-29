# Определение максимального элемента списка
# [1, 2, 3, 4, 5, 0, 2] -> 5
# len() - можно

def recusion_max(numbers: list[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]
    max_number = recusion_max(numbers[1:])
    if numbers[0] > max_number:
        return numbers[0]
    return max_number

print(recusion_max([10001, 2, 3, 4, 5, 0, 2, 1000]))