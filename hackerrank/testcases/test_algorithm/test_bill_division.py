import pytest

from hackerrank.solutions.algorithms.bil_division import bonAppetit

@pytest.mark.parametrize("bill,k,b,expected",[([3,10,2,9],1,12,5),([3,10,2,9],1,7,"Bon Appetit")]
, ids=["TESTCASE1","TESTCASE2"])

def test_bill_division(bill, k, b, expected):
    assert bonAppetit(bill, k, b) == expected