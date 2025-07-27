import pytest
from karatsuba import karatsuba

class TestKaratsuba:
    
    def test_basic_cases(self):
        assert karatsuba(12, 34) == 12 * 34
        assert karatsuba(123, 456) == 123 * 456
        assert karatsuba(1234, 5678) == 1234 * 5678
    
    def test_single_digit(self):
        assert karatsuba(3, 7) == 21
        assert karatsuba(9, 9) == 81
        assert karatsuba(0, 5) == 0
    
    def test_with_zero(self):
        assert karatsuba(0, 123) == 0
        assert karatsuba(456, 0) == 0
        assert karatsuba(0, 0) == 0
    
    def test_large_numbers(self):
        a = 12345678
        b = 87654321
        assert karatsuba(a, b) == a * b
        
        a = 999999999
        b = 111111111
        assert karatsuba(a, b) == a * b
    
    def test_different_lengths(self):
        assert karatsuba(12, 3456) == 12 * 3456
        assert karatsuba(9876, 54) == 9876 * 54
        assert karatsuba(1, 123456789) == 1 * 123456789
    
    def test_power_of_ten(self):
        assert karatsuba(100, 100) == 10000
        assert karatsuba(1000, 1000) == 1000000
    
    def test_edge_cases(self):
        assert karatsuba(1, 1) == 1
        assert karatsuba(10, 10) == 100
        assert karatsuba(99, 99) == 9801

    def test_negative_cases(self):
        assert karatsuba(-9, 9) == -81
        assert karatsuba(-8, -8) == 64
