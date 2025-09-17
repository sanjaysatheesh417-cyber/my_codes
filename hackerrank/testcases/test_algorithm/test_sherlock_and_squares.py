import pytest

from hackerrank.solutions.algorithms.sherlock_and_squares import squares

@pytest.mark.parametrize("a,b,expected", [(24,49,3),(3,9,2),(17,24,0)]
,ids=["testcase1","testcase2","testcase3"])

def test_squares(a,b,expected):
    assert squares(a,b) == expected