import pytest
from src.stack.baekjoon.baekjoon_2504 import calculate

@pytest.mark.parametrize('s', ['(', '([]', '((())'])
def test_returns_0_when_the_length_is_odd(s):
    assert calculate(s) == 0

def test_1():
    assert calculate('()') == 2
    assert calculate('()()') == 4
    assert calculate('()[]') == 5
    assert calculate('(()[])') == 10
    assert calculate('(()[[]])') == 22
    assert calculate('([)]') == 0
    assert calculate('()()()') == 6
    assert calculate('([[[]]])') == 54
    assert calculate('[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]') == 14_348_907
    assert calculate(']]') == 0
    assert calculate('(]]') == 0
    assert calculate('()]]') == 0
    assert calculate('((') == 0