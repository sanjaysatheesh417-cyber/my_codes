import pytest

from hackerrank.solutions.algorithms.circular_array_rotation import circularArrayRotation

@pytest.mark.parametrize("a,k,queries,expected", [([3,4,5],2,[1,2],[5,3]),([1,2,3],2,[0,1,2],[2,3,1])],
ids = ["Testcase1","Testcase2"])

def test_circular_array_rotation(a, k, queries, expected):
    assert circularArrayRotation(a, k, queries) == expected