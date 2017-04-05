__author__ = 'Administrator'
import mysql.connector
import  configparser
import  urllib.request


#创建连接数据库的类，这个类只有连接数据库并返回cnn
class DataBase:

    def __init__(self,config):
        self.config=config
        cf=configparser.ConfigParser()
        cf.read(self.config)
        self.config=eval(cf["mysql"]["connect"])



    def get_cnn(self):
        cnn=mysql.connector.connect(**self.config)
        return cnn


