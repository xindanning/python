__author__ = 'Administrator'
#4、 新建一个xls,有两列， 分别是name和sex,写入100行数据， 第一列为随机的名字， 第二列为随机的sex（ 1,2）
#使用xlrd读取该excel,统计每个sex的name数量， 并打印出来。
import xlwt3
import random
import  xlrd


def create_value(a,b):#写一个函数，随机生成name和sex
  t=''
  l=random.sample(a,b)
  for i in range(len(l)):#遍历的长度是想要的字符串长度
    t+=l[i]            #t一开始是空的字符串，随机取数据拼接起来，一直拼接到想要的长度
  return t            #t返回给调用它的变量

name=create_value('abcdefg',3)
sex=create_value('01',1)


def insert_value(path):
    workbook_new=xlwt3.Workbook()  #创建一个Excel对象
    sheet_new=workbook_new.add_sheet('create_new_sheet', cell_overwrite_ok=True)
    sheet_new.write(0, 0, "name")
    sheet_new.write(0, 1, "sex")
    for i in range(1,101):
        name=create_value('abcdefg',3)
        sex=create_value('01',1)
        sheet_new.write(i,0,name)
        sheet_new.write(i,1,sex)
        workbook_new.save(path)




def count_sex(path):
    workbook=xlrd.open_workbook(path)
    sheet_obj=workbook.sheet_by_index(0)#按索引读第一个sheet
    c = 0
    d = 0
    for i in range(1,sheet_obj.nrows):
        k=int(sheet_obj.cell_value(i,1))
        if k:
         c=c+1
        else:
         d=d+1
    print(c,d)
    return c,d



insert_value("D://zuoye.xls")
count_sex("D://zuoye.xls")