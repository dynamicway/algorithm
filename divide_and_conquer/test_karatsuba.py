import pytest
from karatuba import karatuba

class TestKaratuba:
    
    def test_basic_cases(self):
        assert karatuba(12, 34) == 12 * 34
        assert karatuba(123, 456) == 123 * 456
        assert karatuba(1234, 5678) == 1234 * 5678
    
    def test_single_digit(self):
        assert karatuba(3, 7) == 21
        assert karatuba(9, 9) == 81
        assert karatuba(0, 5) == 0
    
    def test_with_zero(self):
        assert karatuba(0, 123) == 0
        assert karatuba(456, 0) == 0
        assert karatuba(0, 0) == 0
    
    def test_large_numbers(self):
        a = 12345678
        b = 87654321
        assert karatuba(a, b) == a * b
        
        a = 999999999
        b = 111111111
        assert karatuba(a, b) == a * b
    
    def test_different_lengths(self):
        assert karatuba(12, 3456) == 12 * 3456
        assert karatuba(9876, 54) == 9876 * 54
        assert karatuba(1, 123456789) == 1 * 123456789
    
    def test_power_of_ten(self):
        assert karatuba(100, 100) == 10000
        assert karatuba(1000, 1000) == 1000000
    
    def test_edge_cases(self):
        assert karatuba(1, 1) == 1
        assert karatuba(10, 10) == 100
        assert karatuba(99, 99) == 9801
