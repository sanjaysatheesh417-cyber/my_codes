import pytest

from hackerrank.solutions.algorithms.drawing_book import pageCount

@pytest.mark.parametrize("n,p,expected", [(4,4,0),(5,3,1),(6,2,1),(5,4,0)],
ids=["TESTCASE1","TESTCASE2","TESTCASE3","TESTCASE4"])

def test_pagecount(n,p,expected):
    assert pageCount(n,p) == expected