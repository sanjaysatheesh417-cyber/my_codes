import pytest

from hackerrank.solutions.algorithms.library_fine import libraryFine

@pytest.mark.parametrize("d1, m1, y1, d2, m2, y2,expected", [(9,6,2015,6,6,2015,45),(14,7,2018,5,7,2018,135)]
,ids = ["testcase1","testcase2"])

def test_libraryFine(d1, m1, y1, d2, m2, y2, expected):
    assert libraryFine(d1, m1, y1, d2, m2, y2) == expected