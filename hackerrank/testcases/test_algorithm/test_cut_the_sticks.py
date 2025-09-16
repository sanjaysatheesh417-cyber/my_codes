import pytest

from hackerrank.solutions.algorithms.cut_the_sticks import cutTheSticks

@pytest.mark.parametrize("arr,expected", [([1,2,3],[3,2,1]),([5,4,4,2,2,8],[6,4,2,1]),([1,2,3,4,3,3,2,1]
,[8,6,4,1])], ids=["testcase1","testcase2","testcase3"])

def test_cut_the_sticks(arr, expected):
    assert cutTheSticks(arr) == expected