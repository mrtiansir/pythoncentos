#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from my_python_basic.chapter10_class.class_2_method import Person

class Manager:
    def __init__(self, name, age, pay):
        #为Manager类产生的实例自动产生job为'manager'
        Person.__init__(self, name, age, pay, 'manager')

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)

    def __str__(self):
        return f'<{self.__class__.__name__} => {self.name}, {self.age}, {self.pay}, {self.job}>'

if __name__ == '__main__':
    tom = Manager('Tom Doe', 50, 50000)
    print(tom)
    print(tom.name)
    print(tom.job)


    