import pytest

from hackerrank.solutions.algorithms.electronics_shop import getMoneySpent

@pytest.mark.parametrize("keyboards, drives, b, expected", [([40,50,60],[5,8,12],60,58)
,([3,1],[5,2,8],10,9),([4],[5],5,-1)], ids=["TESTCASE1", "TESTCASE2", "TESTCASE3"])

def test_getMoneySpent(keyboards, drives, b, expected):
    assert getMoneySpent(keyboards, drives, b) == expected