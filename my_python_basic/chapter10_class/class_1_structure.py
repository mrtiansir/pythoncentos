#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

class Person:
    def __init__(self, name, age, pay=0, job=None):   #初始化实例的方法
        self.name = name # self为实例
        self.age = age
        self.pay = pay
        self.job = job



if __name__ == '__main__':
    bob = Person('Bob Smith', 25, 30000, 'software')  #产生实例
    jim = Person('Jim Green', 30, 20000, 'hardware')
    print(bob.name)
    print(jim.pay)

    print(bob.name.split()[-1])  #查询Lastname
    jim.pay *= 1.10   #加薪
    print(jim.pay)

    