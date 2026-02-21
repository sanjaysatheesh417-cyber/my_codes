import pytest

from hackerrank.solutions.algorithms.save_the_prisoner import saveThePrisoner

@pytest.mark.parametrize("n,m,s,expected", [(4,6,2,3),(5,2,1,2),(5,2,2,3),(7,19,2,6),(3,7,3,3)]
,ids = ["testcases1","testcases2","testcases3","testcases4","testcases5"])

def test_save_the_prisoner(n,m,s,expected):
    assert saveThePrisoner(n,m,s) == expected