__author__ = 'Administrator'
import mysql.connector
#1.数据库的配置信息，存到字典里面
config={'host':'120.24.235.105',#默认127.0.0.1
        'user':'student2',
        'password':'student2@',
        'port':3306,
        'database':'python',
        'charset':'utf8'#默认即为utf8
}

#2.创建数据库的链接字符串 cnn
cnn=mysql.connector.connect(**config)#必须有两个星

#3.创建一个游标
cursor=cnn.cursor()

#4.创建数据库
'''sql_creat_table='CREATE TABLE moming\
(id int(10) NOT NULL AUTO_INCREMENT,\
name varchar(10) DEFAULT NULL,\
age int(3) DEFAULT NULL,\
PRIMARY KEY (id))\
ENGINE=MyISAM DEFAULT CHARSET=utf8


try:
    cursor.execute(sql_creat_table)
except mysql.connector.Error as e:
    print('create table orange fails!{}'.format(e))


finally:
'''
#执行插入语句：
'''sql_insert4='insert into moming (id,name,age) values (%s,%s,%s)'
data3=[
(2,'山楂',4),
(4,'鱿鱼',5),
(5,'煎饼',6)]
cursor.executemany(sql_insert4,data3)
'''

#执行查询语句
cursor.execute("select * from moming")
print(cursor.fetchall())







cursor.close()
cnn.close()