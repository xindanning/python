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

#4.查询student1表

cursor.execute("select * from student1")
print(cursor.fetchall())

#5.where条件查询
#sql="select name from student1 where id>%s and age>%s" #%s是一个占位符
#cursor.execute(sql,(1,20,))#固定用法，传参是一个tuple
#print(cursor.fetchone())

#6.加入异常抛错处理
'''try:
  sql="select name from student1 where id=1"
  cursor.execute(sql)
  print(cursor.fetchone())

except mysql.connector.Error as e:
  print('query error:%s'%e)

finally:
  cursor.close()
  cnn.close()
'''

#数据库的插入操作
sql_insert1="insert into student1(name,age) values ('安全第一',1)"
cursor.execute(sql_insert1)  #execute就是执行操作的意思，括号里面参数是sql语句




'''sql_insert2="insert into student1 (name,age) values (%s,%s)"#此处的%s为占位符，而不是格式化字符串，所以age用%s占用一个位置，后期可以直接替换参数。
data1=('莫名',2)
cursor.execute(sql_insert2,data1)
'''

'''sql_insert3="insert into student1 (name,age) valves (%(name)s,%(age)s)"
data2={'name':'莫名','age':3}
cursor.execute(sql_insert3,data2)#如果数据库引擎为innodb，执行完成后需执行cnn.commit()进行事务提交


sql_insert4='insert into student1 (name,age) values (%s,%s)'
data3=[
('莫名',4),
('莫名',5),
('莫名',6)]
cursor.executemany(sql_insert4,data3)
'''


