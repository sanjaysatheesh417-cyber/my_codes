import pytest

from hackerrank.solutions.algorithms.day_of_the_programmer import dayOfProgrammer

@pytest.mark.parametrize("year,expected", [(1984,"12.09.1984"),(2017,"13.09.2017")
,(2016,"12.09.2016"),(1800,"12.09.1800")] ,ids=["TESTCASE1","TESTCASE2","TESTCASE3","TESTCASE4"])

def test_year(year, expected):
    assert dayOfProgrammer(year) == expected