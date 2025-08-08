import pytest

from hackerrank.solutions.algorithms.counting_valleys import countingValleys

@pytest.mark.parametrize("steps,path,expected",[(10,"DDUDDUUDUU",1),(8,"UDDDUDUU",1)]
, ids=["TESTCASE1","TESTCASE2"])

def test_counting_valleys(steps, path, expected):
    assert countingValleys(steps, path) == expected