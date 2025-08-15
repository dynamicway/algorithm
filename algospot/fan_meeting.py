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
    an, bn = len(a), len(b)

    if (an == 0 or bn == 0):
        return []

    if (an < bn):
        return karatsuba(b, a)

    if (bn < 50):
        return multiply(a, b)
    
    split_point = an // 2
    a_left, a_right = split_array(a, split_point)
    b_left, b_right = split_array(b, split_point)

    z2 = karatsuba(a_right, b_right)
    z0 = karatsuba(a_left, b_left)
    z1 = karatsuba(add(a_right, a_left), add(b_right, b_left))
    
    term1 = [0] * (split_point * 2) + z2
    term2 = [0] * split_point + subtract(subtract(z1, z2), z0)
    term3 = z0

    return add(add(term1, term2), term3)

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