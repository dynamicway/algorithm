from src.queue.baekjoon.baekjoon_1158 import josephus

def test_1():
    assert josephus(1, 1) == [1]
    assert josephus(1, 2) == [1]
    assert josephus(2, 1) == [1, 2]
    assert josephus(2, 2) == [2, 1]
    assert josephus(3, 3) == [3, 1, 2]
    assert josephus(3, 4) == [1, 3, 2]
    assert josephus(7, 3) == [3, 6, 2, 7, 5, 1, 4]
    assert josephus(5000, 5000) == []