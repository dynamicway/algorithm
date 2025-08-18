from src.queue.baekjoon.baekjoon_2164 import find_last_card


def test():
    assert find_last_card(1) == 1
    assert find_last_card(6) == 4
    assert find_last_card(2) == 2
    assert find_last_card(500_000) == 475712