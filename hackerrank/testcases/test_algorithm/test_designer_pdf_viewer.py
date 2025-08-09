import pytest

from hackerrank.solutions.algorithms.designer_pdf_viewer import designerPdfViewer

@pytest.mark.parametrize("h,word,expected",
[([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],"abc",9),
 ([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7],"zaba",28)], ids=["TESTCASE1","TESTCASE2"])

def test_designerpdfviewer(h,word,expected):
    assert designerPdfViewer(h,word) == expected