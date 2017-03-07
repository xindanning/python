__author__ = 'Administrator'
day=input("请输入数字")
day=int(day)
if  day==1:
    print("星期一")
elif day==2:
    print("星期二")
elif day==3:
    print("星期三")
elif day==4:
    print("星期四")
elif day==5:
    print("星期五")
elif day==6:
    print("星期六")
elif day==7:
    print("星期日")
else:
    print("请输入1-7的数字")





sum =0
for x in list(range(101)):
    sum=sum+x

print(sum)
#aaaaaa


#完成这个列表的输出a=[5,6,7,9,10,23,45],要求是：把数据按照倒序输出。

a=[5,6,7,8,9,10,23,45]
for x in a[-1::-1]:
    print(x)

