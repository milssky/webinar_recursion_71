# Вычислить сумму элементов списка чисел
# [1,2,3,4,5] -> 15

def recursion_sum(numbers: list[int]) -> int:
    if numbers == []:
        return 0
    return numbers[0] + recursion_sum(numbers[1:])

print(recursion_sum([1,2,3,4,5]))
# a = [1,2,3]
# print(a[:-4])