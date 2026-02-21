import pytest

from hackerrank.solutions.algorithms.jumping_on_clouds_revisited import jumpingOnClouds

@pytest.mark.parametrize("c, k, expected", [([0,0,1,0],2,96),([0, 0, 1, 0, 0, 1, 1, 0],2,92)]
,ids = ["TESTCASE1","TESTCASE2"])

def test_jumpingOnClouds(c, k, expected):
    assert jumpingOnClouds(c, k) == expected