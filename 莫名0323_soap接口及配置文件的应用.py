__author__ = 'Administrator'
from suds.client import Client
import mysql.connector
import configparser


class Test_soap():
     def __init__(self):          #初始化，读取各种需要的配置
        cf=configparser.ConfigParser()
        cf.read("test.conf")
        self.sms_url=cf["soap"]["sms_url"]  #发送验证码的url
        self.reg_url=cf["soap"]["reg_url"]  #注册的url
        self.client_ip=cf["soap"]["client_ip"]
        self.mobile=cf["soap"]["mobile"]
        self.tmpl_id=cf["soap"]["tmpl_id"]
        self.table = cf["mysql"]["table"]
        self.data=eval(cf["user"]["data"] )  #用户信息
        self.config=eval(cf.get("mysql","connect"))  #数据库连接信息

     def soap_sms(self):   #发送验证码
        data_1={"client_ip": self.client_ip, "mobile": self.mobile,"tmpl_id":self.tmpl_id}
        sms_url=self.sms_url
        client_2=Client(sms_url)
        result=client_2.service.sendMCode(data_1)
        print(result)

     def get_verifycode(self):   #获取到验证码
        #config=self.config
        #创建数据库的链接字符串 cnn
        cnn=mysql.connector.connect(**self.config)#必须有两个星
        #创建一个游标
        cursor=cnn.cursor()
        cursor.execute("select Fverify_code from %s"%self.table)
        self.verify_code=cursor.fetchone()
        return self.verify_code
        cursor.close()
        cnn.close()



     def soap_reg(self):      #进行注册操作
         data_varifycode={"verify_code":self.verify_code}
         data_2=dict(self.data,**data_varifycode)    #将验证码和其他配置文件里的信息拼接成新的字典
         reg_url=self.reg_url
         client_3=Client(reg_url)
         #print(client_3)
         result=client_3.service.userRegister(data_2)
         print(result)


#创建实例并调用方法
test_1 = Test_soap()
test_1.soap_sms()
test_1.get_verifycode()
result=test_1.soap_reg()
print(result)


'''
#1.调用suds库，完成发送验证码的请求
sms_url="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
client_2=Client(sms_url)
#print(client_2)
data = {"client_ip": "192.168.5.6", "mobile": "13947015925", "tmpl_id":" 1"}
result=client_2.service.sendMCode(data)
print(result)





#2.用select语句，在数据库中查找到验证码，将验证码存储到变量里
config={'host':'120.24.235.105',#默认127.0.0.1
        'user':'student2',
        'password':'student2@',
        'port':3306,
        'database':'sms_db_25',
        'charset':'utf8'#默认即为utf8
}
#创建数据库的链接字符串 cnn
cnn=mysql.connector.connect(**config)#必须有两个星
#创建一个游标
cursor=cnn.cursor()
cursor.execute("select Fverify_code from t_mvcode_info_9 where Fmobile_no=13947015925")
t=cursor.fetchone()
cursor.close()
cnn.close()




#3.把需要的参数放进字典里
data={"verify_code":t,"user_id":"moming_1","channel_id":"1","pwd":"123456","mobile":"13947015925","ip":"192.168.30.40"}




#4.进行注册操作
sms_url="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl "
client_3=Client(sms_url)
#print(client_3)
result=client_3.service.userRegister(data)
print(result)



#配置文件的用法
cf=configparser.ConfigParser()    #创建一个对象
cf.read("test.conf" )

#sections返回数据片段，如[mysql],看配置文件中有哪些片段
s=cf.sections()
print(s)

#options(sections）返回指定片段里的所有options(参数名key)
name=cf.options("mysql")
print(name)

#items(section)返回指定片段里的所有key和value
value=cf.items("mysql")
print(value)

#get()返回片段里的具体数据,类型为String
db_host=cf.get("mysql","host")
db_password=cf.get("mysql","password")
print(db_host,db_password)


#另一种常用的读取数据的方法
db_host=cf["mysql"]["host"]
print(db_host)
'''
