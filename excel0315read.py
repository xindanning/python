__author__ = 'Administrator'
import  xlrd
path="D:\\test.xls"
workbook=xlrd.open_workbook(path)


sheet_obj_1=workbook.sheet_by_index(1)
row_number=sheet_obj_1.nrows
col_number=sheet_obj_1.ncols

print("所有的行数",row_number)
print("所有的列数",col_number)


a=sheet_obj_1.cell_value(5,1)
b=sheet_obj_1.cell_value(7,2)
c=sheet_obj_1.cell_value(1,3)
print(a,b,c)
