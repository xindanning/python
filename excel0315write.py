__author__ = 'Administrator'
import xlwt3


workbook_new=xlwt3.Workbook()  #创建一个Excel对象
sheet_new=workbook_new.add_sheet('create_new_sheet', cell_overwrite_ok=True)#加入cell_overwrite_ok=True保证数据在重写时不会报错
sheet_new.write(0, 0, "name")
sheet_new.write(0, 1, "sex")
sheet_new.write(1, 0, "moming")
sheet_new.write(1, 1, "23")
workbook_new.save("D:\\write.xls")

