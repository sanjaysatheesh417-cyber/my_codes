import pytest

from hackerrank.solutions.algorithms.jumping_on_the_clouds import jumpingOnClouds

@pytest.mark.parametrize("c,expected", [([0,0,0,0,1,0],3),([0,0,1,0,0,1,0],4),([0,1,0,0,0,1,0],3)])

def test_jumpingOnClouds(c, expected):
    assert jumpingOnClouds(c) == expected