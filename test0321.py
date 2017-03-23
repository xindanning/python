__author__ = 'Administrator'
import  urllib.request
import  urllib.parse    #引入模块对数据进行转码


#直接访问方式
url_1="https://www.baidu.com"
response_1=urllib.request.urlopen(url_1)
print("返回的状态码是：",response_1.getcode())



#请求参数封装在字典里的方式
url_2="http://v.juhe.cn/laohuangli/d"
data_1={"key":"a8f2732319cf0ad3cce8ec6ef7aa4f33","date":"2017-03-21"}#将请求参数封装在字典里
data_1=urllib.parse.urlencode(data_1) #转码

url_2=url_2+"?"+data_1     #拼接的固定写法

response_2=urllib.request.urlopen(url_2)
result_2=response_2.read()      #读取内容，非状态码
result_2=result_2.decode("utf-8")#将内容进行汉字转化
print(result_2)



#post请求的方式
url_3="http://v.juhe.cn/laohuangli/d"
data_2={"key":"a8f2732319cf0ad3cce8ec6ef7aa4f33","date":"2017-03-21"}#将请求参数封装在字典里
data_2=urllib.parse.urlencode(data_2) #转码
data_2=data_2.encode("utf-8") #编码

req=urllib.request.Request(url_3,data_2)   #拼接地址与参数,预处理
response_3=urllib.request.urlopen(req)
result_3=response_3.read()      #读取内容，非状态码
result_3=result_3.decode("utf-8")#将内容进行汉字转化
print(result_3)


