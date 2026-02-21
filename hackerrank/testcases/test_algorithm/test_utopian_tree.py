import pytest

from hackerrank.solutions.algorithms.utopian_tree import utopianTree

@pytest.mark.parametrize("n,expected",[(0,1),(1,2),(4,7),(5,14)]
, ids=["TESTCASE1","TESTCASE2","TESTCASE3","TESTCASE4"])

def test_utopianTree(n, expected):
    assert utopianTree(n) == expected