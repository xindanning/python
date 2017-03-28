__author__ = 'Administrator'
#写一个类： Math， 要求如下：
#1） 有一个初始化函数， 有一个参数 以及一个默认参数。
#2） 有4个方法， 分别是加减乘除。
#3） 创建实例来进行调用



class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def jia(self):
        return (self.a+self.b)

    def jian(self):
        return(self.a-self.b)

    def cheng(self):
        return(self.a*self.b)

    def chu(self):
        return(self.a/self.b)


math_1=Math(2,4)
math_1.jia()
math_1.jian()
math_1.cheng()
math_1.chu()
print(math_1.jia())
'''
#第二题：
#写一个类：倒序排列某个字符串， 要求如下：
#1)有一个初始化函数， 传递你需要倒序排列的字符串；
#2） 有一个类方法， 用来达到倒序排列的效果
#3） 创建实例来调用。


class Daoxu():
    def __init__(self,a):
        self.a=a

    def pailie(self):
       print(self.a[::-1])


c=Daoxu("asdffjgkl")
c=c.pailie()
'''

