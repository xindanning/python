__author__ = 'Administrator'
#一、 对http类型的接口测试进行封装，封装成类，要求如下：
#1）类里面包含get和post请求两个函数；
#2）创建实例来进行调用
import  urllib.request
import  urllib.parse    #引入模块对数据进行转码
import configparser

class TestInterface:
    def __init__(self):
        cf=configparser.ConfigParser()
        cf.read("test.conf")
        self.key=cf["http"]["key"]
        self.date=cf["http"]["date"]
        self.url=cf["http"]["url"]


    def interface_get(self):
        data_1={"key":self.key,"date":self.date}#将请求参数封装在字典里
        data_1=urllib.parse.urlencode(data_1) #转码
        url_1=self.url+"?"+data_1

        response_1=urllib.request.urlopen(url_1)
        result_1=response_1.read()
        result_1=result_1.decode('utf-8')
        return result_1


    def interface_post(self):
        url_2=self.url
        data_2={"key":self.key,"date":self.date}#将请求参数封装在字典里
        data_2=urllib.parse.urlencode(data_2) #转码
        data_2=data_2.encode('utf-8')
        req_2=urllib.request.Request(url_2,data_2)#拼接地址与参数，预处理

        response_2=urllib.request.urlopen(req_2)
        result_2=response_2.read()
        result_2=result_2.decode('utf-8')
        return result_2


#get_1=TestInterface("http://v.juhe.cn/laohuangli/d","a8f2732319cf0ad3cce8ec6ef7aa4f33","2017-03-21")
get_1 = TestInterface()
print("get请求结果为", get_1.interface_get())
print("post请求结果为", get_1.interface_post())











