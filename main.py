# 1
from collections import Counter


def lab1(array):
    pair_elements = set(k for k, v in Counter(array).items() if not v % 2)
    pair_only_array = [x for x in array if x in pair_elements]
    return pair_only_array


# 2
def lab2(array):
    return [array[i::4] for i in range(4)]


# 3
def lab3(array):
    def fib(lst):
        a, b = 0, 1
        while lst:
            yield lst[:a]
            lst = lst[a:]
            a, b = b, a + b

    return list(fib(array))
