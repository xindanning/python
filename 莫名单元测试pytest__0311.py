__author__ = 'Administrator'
import pytest
from learnpython.莫名0309类 import Math


def test_main():
    x=Math(2,3).jia()
    assert x==5
if __name__=='__main__':
    pytest.main("C:/Users/Administrator/PycharmProjects/untitled3/learnpython/莫名pytest_0311.py --pastebin=all")


