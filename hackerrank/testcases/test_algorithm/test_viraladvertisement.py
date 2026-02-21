import pytest

from hackerrank.solutions.algorithms.viral_advertisement import viralAdvertising

@pytest.mark.parametrize("n,expected", [(5,24),(3,9)] ,ids=["testcases1","testcases2"])

def test_viralAdvertising(n,expected):
    assert viralAdvertising(n) == expected