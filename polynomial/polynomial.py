
from itertools import zip_longest


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
    
    return result

def add(a, b):
    return [x + y for x, y in zip_longest(a, b, fillvalue=0)]