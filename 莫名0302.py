__author__ = 'Administrator'
#.本节课作业

#1:把a 和b的值一起组合打印出来，a=[1,2,3,"this is a list"]，b=[4,5,6,"这是第二个列表"]
a=[1,2,3,"this is a list"]
b=[4,5,6,"这是第二个"]
print(a+b)

#2：输出列表a两次
print(a,a)

#3：取a列表第3个值
print(a[2])

#4：取b列表第2个和第3个值
print(b[1],b[2])

#5：取a列表第三个值以及到末尾的所有值
print(a[2:])


#6：L = [
#['Apple', 'Google', 'Microsoft'],
#['Java', 'Python', 'Ruby', 'PHP'],
#['Adam', 'Bart', 'Lisa']
#]
#打印Apple、 Python、 Lisa

L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]


print(L[0][0])
print(L[1][1])
print(L[2][2])


#7.合并下面的两个list并去重（去重可以使用set函数）
#list1 = [2, 3, 8, 4, 9, 5, 6]
#list2 = [5, 6, 10, 17, 11, 2]

list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list3 = list1+list2

print(list3)
print(set(list3))

#8：a=5,b=9,如何交换这两个值
a=5
b=9
a,b=b,a
print('a =',a)
print('b =',b)

#9:s="lemon ptyhon",如何打印这个字符串两次

s="lemon ptyhon"
print(s,s)


#10：输入一个标准的日期如(20160503)，打印对应的年月日即2016年05月03日[提示：input函数，自行了解]

T=input("请输入时间:")
print(T[:4]+"年"+T[4:6]+"月"+T[6:]+"日")




