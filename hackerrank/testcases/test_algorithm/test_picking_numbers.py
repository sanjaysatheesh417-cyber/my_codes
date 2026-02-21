import pytest

from hackerrank.solutions.algorithms.picking_numbers import pickingNumbers

@pytest.mark.parametrize("a,expected", [([1,1,2,2,4,4,5,5,5],5),([4,6,5,3,3,1],3),
([1,2,2,3,1,2],5)] ,ids=["TESTCASE1","TESTCASE2","TESTCASE3"])

def test_pickingNumbers(a, expected):
    assert pickingNumbers(a) == expected