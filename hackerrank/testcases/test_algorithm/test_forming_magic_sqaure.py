import pytest

from hackerrank.solutions.algorithms.forming_a_magic_square import formingMagicSquare

@pytest.mark.parametrize("s,expected",[([[5, 3, 4], [1, 5, 8], [6, 4, 2]],7),
([[4,9,2],[3,5,7],[8,1,5]],1),([[4,8,2],[4,5,7],[6,1,6]],4)], ids=["TESTCASE1","TESTCASE2","TESTCASE3"])

def test_formingMagicSquare(s, expected):
    assert formingMagicSquare(s) == expected