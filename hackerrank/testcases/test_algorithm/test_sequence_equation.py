import pytest

from hackerrank.solutions.algorithms.sequence_equation import permutationEquation

@pytest.mark.parametrize('p,expected', [([2,3,1],[2,3,1]),([4,3,5,1,2],[1,3,5,4,2]),([5,2,1,3,4],
[4,2,5,1,3])], ids=["TESTCASE1", "TESTCASE2", "TESTCASE3"])

def test_sequence_equation(p,expected):
    assert permutationEquation(p) == expected