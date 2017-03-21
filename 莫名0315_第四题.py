__author__ = 'Administrator'
#4、 新建一个xls,有两列， 分别是name和sex,写入100行数据， 第一列为随机的名字， 第二列为随机的sex（ 1,2）
import xlwt3
import random
import  xlrd



#创建Excel
workbook_new=xlwt3.Workbook()  #创建一个Excel对象
sheet_new=workbook_new.add_sheet('create_new_sheet', cell_overwrite_ok=True)

sheet_new.write(0, 0, "name")
sheet_new.write(0, 1, "sex")

for i in range(1,100):
    sheet_new.write(i,0,''.join(random.sample('abcdefghijklmnopqrst',3)))
for j in range(1,100):
    sheet_new.write(j,1,(random.randint(1,2)))


workbook_new.save("D:\\momingzuoye.xls")




#读取Excel

workbook=xlrd.open_workbook("D:\\momingzuoye.xls")

sheet_obj=workbook.sheet_by_index(0)#按索引读第一个sheet

for i in range(1,sheet_obj.nrows):
      k=sheet_obj.cell_value(i,1)
      man_count=0
      women_count=0
      if (k==1):
         man_count=man_count+1
      else:
         women_count=women_count+1

print("性别为男的人数有",man_count)
print("性别为女的人数有",women_count)