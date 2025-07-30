from itertools import zip_longest
import sys


def solve(members, fans):
    if len(fans) < len(members):
        return 0
    
    f = [1 if s == 'M' else 0 for s in fans][::-1]
    m = [1 if s == 'M' else 0 for s in members]
    result = karatsuba(f, m)
    
    start = len(members) - 1
    end = len(result) - (len(members) - 1)

    count = 0
    for i in range(start, end):
        if result[i] == 0:
            count += 1
    
    return count


def karatsuba(a, b):
    if (len(a) < 50 or len(b) < 50):
        return multiply(a, b)
    
    split_point = get_split_point(a, b)
    a0, a1 = split_array(a, split_point)
    b0, b1 = split_array(b, split_point)

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)
    z1 = karatsuba(add(a1, a0), add(b1, b0))
    
    term1 = [0] * (split_point * 2) + z2
    term2 = [0] * split_point + subtract(subtract(z1, z2), z0)
    term3 = z0

    return add(add(term1, term2), term3)


def get_split_point(a, b):
    return max(len(a), len(b)) // 2

def split_array(arr, split_point):
    return arr[:split_point], arr[split_point:]

def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
    
    return result

def add(a, b):
    return [x + y for x, y in zip_longest(a, b, fillvalue=0)]

def subtract(a, b):
    return [x - y for x, y in zip_longest(a, b, fillvalue=0)]

def main():
    input = sys.stdin.readline
    C = int(input())
    for _ in range(C):
        members = input().strip()
        fans = input().strip()
        print(solve(members, fans))

if __name__ == "__main__":
    main()