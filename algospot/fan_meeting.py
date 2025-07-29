from polynomial.polynomial import add, multiply, subtract

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
    a_high, a_low = split_array(a, split_point)
    b_high, b_low = split_array(b, split_point)

    z0 = karatsuba(a_low, b_low)
    z1 = karatsuba(add(a_high, a_low), add(b_high, b_low))
    z2 = karatsuba(a_high, b_high)
    
    term1 = z2 + [0] * (split_point ** 2)
    term2 = subtract(subtract(z1, z2), z0) + [0] * split_point
    term3 = z0

    return add(add(term1, term2), term3)


def get_split_point(a, b):
    return max(len(a), len(b)) // 2

def split_array(arr, split_point):
    return arr[:split_point], arr[split_point:]