import pytest

from hackerrank.solutions.algorithms.hurdle_race import hurdleRace

@pytest.mark.parametrize("k,height,expected",[(1,[1,2,3,3,2],2),(4,[1,6,3,5,2],2),(7,[2,5,4,5,2],0)]
, ids=["TESTCASE1","TESTCASE2","TESTCASE3"])

def test_hurdleRace(k, height, expected):
    assert hurdleRace(k, height) == expected
