__author__ = 'Administrator'

class Person():
   def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex



   def sing(self):
       print("我叫",self.name+"今年",self.age,"我喜欢唱歌")

   def m(self,m1,s):
        print("我每天跑",m1,"米",s,"秒")

person1=Person("moming",23,"女")
person1.sing()
person1.m(500,30)


class Child(Person):
     pass



child_1=Child("moming",23,"女")
