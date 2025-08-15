from divide_and_conquer.karatsuba import karatsuba
    
def test_basic_cases():
    assert karatsuba(12, 34) == 12 * 34
    assert karatsuba(123, 456) == 123 * 456
    assert karatsuba(1234, 5678) == 1234 * 5678

def test_single_digit():
    assert karatsuba(3, 7) == 21
    assert karatsuba(9, 9) == 81
    assert karatsuba(0, 5) == 0

def test_with_zero():
    assert karatsuba(0, 123) == 0
    assert karatsuba(456, 0) == 0
    assert karatsuba(0, 0) == 0

def test_large_numbers():
    a = 12345678
    b = 87654321
    assert karatsuba(a, b) == a * b
    
    a = 999999999
    b = 111111111
    assert karatsuba(a, b) == a * b

def test_different_lengths():
    assert karatsuba(12, 3456) == 12 * 3456
    assert karatsuba(9876, 54) == 9876 * 54
    assert karatsuba(1, 123456789) == 1 * 123456789

def test_power_of_ten():
    assert karatsuba(100, 100) == 10000
    assert karatsuba(1000, 1000) == 1000000

def test_edge_cases():
    assert karatsuba(1, 1) == 1
    assert karatsuba(10, 10) == 100
    assert karatsuba(99, 99) == 9801

def test_negative_cases():
    assert karatsuba(-9, 9) == -81
    assert karatsuba(-8, -8) == 64
