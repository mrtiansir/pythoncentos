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

    def getraise(self, percent):      #添加加薪的行为
        self.pay *= (1.1 + percent)      #调用giveraise方法的人并不需要知道到底做了哪些修改，他们只需要知道怎么用就行了，实际上方法中对数据的处理已经发生的变化


if __name__ == '__main__':
    bob = Person('Bob Smith', 25, 20000, 'software')
    jim = Person('Jim Green', 30, 30000, 'hardware')
    print(bob.getlastname())
    jim.getraise(0.1)
    print(jim.pay)
