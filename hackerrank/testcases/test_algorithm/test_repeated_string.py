import pytest

from hackerrank.solutions.algorithms.repeated_string import repeatedString

@pytest.mark.parametrize('s,n,expected', [("aba",10,7),("a",1000000000000,1000000000000)
,("abcac",10,4)], ids=["testcase1","testcase2","testcase3"])

def test_repeatedString(s, n, expected):
    assert repeatedString(s, n) == expected