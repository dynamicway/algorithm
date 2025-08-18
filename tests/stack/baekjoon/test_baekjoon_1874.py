import pytest
from stack.baekjoon.baekjoon_1874 import generate_stack_operations


def test_can_generate():
    assert generate_stack_operations(1, [1]) == ["+", "-"]
    assert generate_stack_operations(2, [1, 2]) == ["+", "-", "+", "-"]
    assert generate_stack_operations(2, [2, 1]) == ["+", "+", "-", "-"]
    assert generate_stack_operations(3, [2, 1, 3]) == ["+", "+", "-", "-", "+", "-"]
    assert generate_stack_operations(8, [4, 3, 6, 8, 7, 5, 2, 1]) == [
        "+",
        "+",
        "+",
        "+",
        "-",
        "-",
        "+",
        "+",
        "-",
        "+",
        "+",
        "-",
        "-",
        "-",
        "-",
        "-",
    ]


def test_cannot_generate():
    with pytest.raises(ValueError, match="Impossible sequence"):
        generate_stack_operations(3, [3, 1, 2])