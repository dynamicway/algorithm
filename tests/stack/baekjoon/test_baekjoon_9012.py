from stack.baekjoon.baekjoon_9012 import is_valid_ps

def test_1():
    assert is_valid_ps('()') == True
    assert is_valid_ps('(())') == True
    assert is_valid_ps('())') == False
    assert is_valid_ps('))') == False