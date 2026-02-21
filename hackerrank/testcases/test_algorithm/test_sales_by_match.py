import pytest

from hackerrank.solutions.algorithms.sales_by_match import sockMerchant

@pytest.mark.parametrize('n, ar, expected', [(7,[1,2,1,2,1,3,2],2),(9,[10, 20, 20, 10, 10, 30, 50, 10, 20],3)]
,ids=["TESTCASE1","TESTCASE2"])

def test_sockMerchant(n, ar, expected):
    assert sockMerchant(n, ar) == expected