def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b
    
    split_point = get_split_point(a, b)

    a_high = a // split_point
    a_low = a % split_point
    b_high = b // split_point
    b_low = b % split_point

    z0 = karatsuba(a_low, b_low)
    z1 = karatsuba(a_high + a_low, b_high + b_low)
    z2 = karatsuba(a_high, b_high)

    return split_point ** 2 * z2 + split_point * (z1 - z2 - z0) + z0
    
    
def get_split_point(a, b):
    max_length = max(len(str(a)), len(str(b)))
    return 10 ** (max_length // 2)