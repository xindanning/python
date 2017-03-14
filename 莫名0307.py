__author__ = 'Administrator'
#1：对任意数字列表， 编写一个函数 ， 实现 用冒泡排序法 ，对 list进行一个排序 。


def maopao(a):
  for i in range(0,len(a)):
     for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
  print(a)


maopao(a=[2,32,6,34,21,31,13])


#2：对任意字符串 ， 编写一个函数 ， 实现转换成一个列表 ，每个字符对应列表里面的一个元素 。 要求：用到异常处理。
try:
  def p(a):
      b=[]
      for x  in a:
             b.append(x)

      print(b)
  p(kjlhkj)
except Exception as e:
    print("错误是：",e)
