import pytest

from hackerrank.solutions.algorithms.Beautiful_day_at_movies import beautifulDays

@pytest.mark.parametrize("i, j, k, expected", [(20,23,6,2)])

def test_beautiful_day_at_movies(i, j, k, expected):
    assert beautifulDays(i, j, k) == expected