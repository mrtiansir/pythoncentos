#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getlastname(self):           #添加查询Lastname的行为（method)
        return self.name.split()[-1]

    def giveraise(self, percent):      #添加加薪的行为
        self.pay *= (1.0 + percent)

    def __str__(self):
        return f'<{self.__class__.__name__} => {self.name}, {self.age}, {self.pay}, {self.job}>'   #格式化打印初始化的实例的类名称，及各属性值
    


if __name__ == '__main__':
    bob = Person('Bob Smith', 25, 20000, 'software')
    jim = Person('Jim Green', 30, 30000, 'hardware')
    print(bob)
    print(jim)

