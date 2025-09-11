import pytest

from hackerrank.solutions.algorithms.append_and_delete import appendAndDelete

@pytest.mark.parametrize("s, t, k, expected", [(["a","b","c"],["d","e","f"],6,"Yes")
,("hackerhappy","hackerrank",9,"Yes"),("ashley","ash",2,"No")]
,ids=["testcase1","testcase2","testcase3"])

def test_append_and_delete(s, t, k, expected):
    assert appendAndDelete(s, t, k) == expected