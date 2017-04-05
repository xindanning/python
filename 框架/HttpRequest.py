__author__ = 'Administrator'
import urllib.request
import urllib.parse    #引入模块对数据进行转码
import configparser

class TestInterface:
    def __init__(self,config):
        cf = configparser.ConfigParser()
        cf.read(config)
        self.host = cf["http"]["host"]
        self.port = cf["http"]["port"]

    def interface_get(self, url, data):
        data = urllib.parse.urlencode(data)   # 转码
        url = self.host+":"+self.port+url+"?"+data

        response_1 = urllib.request.urlopen(url)
        result_1=response_1.read()
        result_1 = result_1.decode('utf-8')
        print("GET请求的结果是", result_1)
        return result_1

    def interface_post(self, url, data):
        data = urllib.parse.urlencode(data) #转码
        data = data.encode('utf-8')
        url = self.host+":"+self.port+url
        req_2 = urllib.request.Request(url, data)#拼接地址与参数，预处理

        response_2 = urllib.request.urlopen(req_2)
        result_2 = response_2.read()
        result_2 = result_2.decode('utf-8')
        print("POST请求的结果是", result_2)
        return result_2


#get_1=TestInterface("http://v.juhe.cn/laohuangli/d","a8f2732319cf0ad3cce8ec6ef7aa4f33","2017-03-21")
#get_1 = TestInterface()

