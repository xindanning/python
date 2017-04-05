__author__ = 'Administrator'
import unittest

class Http_Unittest(unittest.TestCase):
    def __init__(self,method,http,url,data):
        super(Http_Unittest,self).__init__(method)     #超继承，固定写法
        
