def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b
    
    mid = get_mid(a, b)

    a0 = a // mid
    a1 = a % mid
    b0 = b // mid
    b1 = b % mid

    z0 = karatsuba(a1, b1)
    z1 = karatsuba(a0 + a1, b0 + b1)
    z2 = karatsuba(a0, b0)

    return mid ** 2 * z2 + mid * (z1 - z2 - z0) + z0
    
    
def get_mid(a, b):
    max_ren = max(len(str(a)), len(str(b)))
    return 10 ** (max_ren // 2)