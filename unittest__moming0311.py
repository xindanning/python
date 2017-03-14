__author__ = 'Administrator'

#unittest 实现单元测试
import unittest  #引入unittest 框架
from learnpython.test0311 import TestMath    #from...import

suite=unittest.TestSuite()
suite.addTest(TestMath("test_jia"))
suite.addTest(TestMath("test_jian"))
suite.addTest(TestMath("test_cheng"))
suite.addTest(TestMath("test_chu"))

runner=unittest.TextTestRunner()
runner.run(suite)