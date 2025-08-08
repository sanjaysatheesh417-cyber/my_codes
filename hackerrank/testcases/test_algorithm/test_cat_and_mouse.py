import pytest

from hackerrank.solutions.algorithms.cat_and_mouse import catAndMouse

@pytest.mark.parametrize("x,y,z,expected", [(1,3,2,"Mouse C"),(1,2,3,"Cat B"),(2,5,4,"Cat B")]
, ids=["TESTCASE1", "TESTCASE2", "TESTCASE3"])

def test_cat_and_mouse(x, y, z, expected):
    assert catAndMouse(x, y, z) == expected