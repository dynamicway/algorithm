from stack.baekjoon.baekjoon_10799 import count_pieces

def test_empty_layout():
    assert count_pieces("") == 0

def test_only_laser():
    assert count_pieces("()") == 0
    assert count_pieces("()()") == 0
    assert count_pieces("()()()") == 0

def test_cuts_one_bar():
    assert count_pieces("(())") == 2
    assert count_pieces("((()))") == 4

def test_cuts_two_separate_bars():
    assert count_pieces("(())(())") == 4
    assert count_pieces("((()))(())") == 6

def test_cuts_nested_bars():
    assert count_pieces("(()())") == 3
    assert count_pieces("(()(()))") == 5
    assert count_pieces("((()(()))") == 8
    assert count_pieces("()(((()())(())()))(())") == 17
    assert count_pieces("(((()(()()))(())()))(()())") == 24