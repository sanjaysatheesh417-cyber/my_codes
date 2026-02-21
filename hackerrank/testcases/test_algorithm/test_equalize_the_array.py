import pytest

from hackerrank.solutions.algorithms.equalize_the_array import equalizeArray

@pytest.mark.parametrize("arr,expected", [([1,2,2,3],2),([3,3,2,1,3],2)]
,ids = ["testcase1","testcase2"])

def test_equalize_the_array(arr, expected):
    assert equalizeArray(arr) == expected