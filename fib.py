# 1 1 2 3 5 8 13 ...
# 1 2 3 4 5 6  
from functools import lru_cache

result = {}

def fib(n):
    if n in result:
        return result[n]
    if n in (1, 2):
        return 1
    res = fib(n - 1) + fib(n - 2)
    result[n] = res
    return res



@lru_cache
def fib_cache(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(500))
# print(len(result.items()))
print(fib_cache(500))
print(fib(500))
