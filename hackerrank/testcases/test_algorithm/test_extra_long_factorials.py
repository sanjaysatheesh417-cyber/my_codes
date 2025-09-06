import pytest

from hackerrank.solutions.algorithms.Extra_long_factorials import extraLongFactorials

@pytest.mark.parametrize("n, expected", [(30,265252859812191058636308480000000)
,(25,15511210043330985984000000)],ids=["testcase1","testcase2"])

def test_extra_long_factorials(n, expected):
    assert expected == extraLongFactorials(n)