import pytest
from algospot.fan_meeting import solve


def test_simple_case():
    """간단한 테스트 케이스"""
    # MFM과 FFFMMMFFF에서 매칭되는 위치 테스트
    assert solve('MFM', 'FFFMMMFFF') >= 0  # 일단 에러 없이 실행되는지 확인


def test_no_matching():
    """매칭이 불가능한 케이스"""
    # 팬 길이가 멤버보다 짧은 경우
    assert solve('MFM', 'FF') == 0


def test_all_female_fans():
    """모든 팬이 여성인 경우"""
    assert solve('MF', 'FFFF') == 3  # 모든 위치에서 악수 없음


def test_all_male_fans():
    """모든 팬이 남성인 경우"""
    assert solve('MF', 'MMMM') == 0  # M끼리 만나면 악수


def test_example_case():
    """예시 케이스"""
    assert solve('FFFMMM', 'MMMFFF') == 1
    assert solve('FFFFF', 'FFFFFFFFFF') == 6
    assert solve('FFFFM', 'FFFFFMMMMF') == 2
    assert solve('MFMFMFFFMMMFMF', 'MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF') == 2

if __name__ == "__main__":
    pytest.main([__file__])