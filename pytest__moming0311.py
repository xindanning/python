__author__ = 'Administrator'
import pytest
from learnpython.test0311 import TestMath


def test_jia():
    x=TestMath(1,4).test_jia()
    assert x==5
if __name__=='__main__':
    pytest.main('C:/Users/Administrator/PycharmProjects/untitled3/learnpython/pytest__moming0311.py--pastebin=all')


