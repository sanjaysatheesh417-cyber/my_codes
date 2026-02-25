import pytest

from hackerrank.solutions.algorithms.Taum_and_Bday import taumBday

@pytest.mark.parametrize("b,w,bc,wc,z,expected",[(10,10,1,1,1,20),(5,9,2,3,4,37),(3,6,9,1,1,12),
                                                 (7,7,4,2,1,35),(3,3,1,9,2,12)] ,
                         ids = ["TESTCASE1","TESTCASE2","TESTCASE3","TESTCASE4","TESTCASE5"])
def taum_and_bday(b,w,bc,wc,z,expected):
    assert taumBday(b,w,bc,wc,z) == expected