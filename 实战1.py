__author__ = 'Administrator'
import mysql.connector
import  configparser
import  urllib.request

class Cnn_mysql:

    def __init__(self):
        cf=configparser.ConfigParser()
        cf.read("shizhan1.conf")
        self.config=cf["mysql"]["connect"]
        self.sql=cf["mysql"]["sql"]


    def connect_mysql(self):
        cnn=mysql.connector.connect(**self.config)
        cursor=cnn.cursor()
        cursor.execute(sql)
        sql=
        cursor.close()
        cnn.close()


