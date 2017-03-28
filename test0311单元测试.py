__author__ = 'Administrator'
import unittest
from learnpython.莫名0309类 import Math

class TestMath(unittest.TestCase):

       def test_jian(self):
            try:
                tester=Math(2,4)
                result_jian=tester.jian()
                self.assertEqual(result_jian,-2,"答案不等于-2，错误")
            except AssertionError as e:
                 print("错误是"%e)


       def test_jia(self):
            tester=Math(2,4)
            result_jia=tester.jia()
            self.assertEqual(result_jia,6,"答案不等于6，错误")


       def test_cheng(self):
            tester=Math(2,4)
            result_cheng=tester.cheng()
            self.assertEqual(result_cheng,8,"答案不等于8，错误")


       def test_chu(self):
            tester=Math(2,4)
            result_chu=tester.chu()
            self.assertEqual(result_chu,0.5,"答案不等于0.5，错误")

