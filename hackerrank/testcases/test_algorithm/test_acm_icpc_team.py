import pytest

from hackerrank.solutions.algorithms.ACM_ICPC_team import acmTeam

@pytest.mark.parametrize("topic,expected",[(["10101","11110","00010"],[5,1]),
(["10101","11100","11010","00101"],[5,2])])

def test_acmTeam(topic, expected):
    assert acmTeam(topic) == expected