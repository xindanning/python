__author__ = 'Administrator'

#unittest 实现单元测试
import unittest  #引入unittest 框架
from learnpython.test0311单元测试 import TestMath    #from...import

suite=unittest.TestSuite()         #创建测试集实例
suite.addTest(TestMath("test_jia"))         #固定写法，指明添加的是哪个测试类下的什么测试方法
suite.addTest(TestMath("test_jian"))
suite.addTest(TestMath("test_cheng"))
suite.addTest(TestMath("test_chu"))

runner=unittest.TextTestRunner()        #创建执行的实例
runner.run(suite)