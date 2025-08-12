import pytest

from hackerrank.solutions.algorithms.Angry_professor import angryProfessor

@pytest.mark.parametrize("k,a,expected", [(3,[-2,-1,0,1,2],"NO"),(3,[-1,-3,4,2],"YES"),
(2,[0,-1,2,-1],"NO")] ,ids=["TESTCASE1","TESTCASE2","TESTCASE3"])

def test_angryprofessor(k,a,expected):
    assert angryProfessor(k,a) == expected