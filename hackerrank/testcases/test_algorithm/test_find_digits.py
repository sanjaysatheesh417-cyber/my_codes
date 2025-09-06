import pytest

from hackerrank.solutions.algorithms.find_digits import findDigits

@pytest.mark.parametrize("n,expected",[(124,3),(111,3),(10,1),(12,2),(1012,3)]
,ids =["TESTCASE1","TESTCASE2","TESTCASE3","TESTCASE4","TESTCASE5"])

def test_find_digits(n, expected):
    assert expected == findDigits(n)