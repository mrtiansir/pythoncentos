#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getlastname(self):
        return self.name.split()[-1]

    def getfirstname(self):
        return self.name.split()[0]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return f'<{self.__class__.__name__} => {self.name}, {self.age}, {self.pay}, {self.job}>'

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)

    def __str__(self):
        return f'<{self.__class__.__name__} => {self.name}, {self.age}, {self.pay}, {self.job}>'


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    jim = Person('Jim Green', 45, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)
    db = [bob, jim, tom]
    for obj in db:
        print(obj)
        print(obj.name + "的姓为: " + obj.getlastname())
        print(obj.name + "的名为: " + obj.getfirstname())
        obj.giveraise(0.1)
        print(f'{obj.name:<10s} "加薪10%后的pay为:" {obj.pay:<10.2f}')
        print('='*60)


    