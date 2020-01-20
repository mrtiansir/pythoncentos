#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

from my_python_basic.chapter10_class.class_2_method import Person
from my_python_basic.chapter10_class import Manager

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000)
    sue = Person('Sue Jones', 45, 40000)
    tom = Manager('Tom Doe', 50, 50000)
    db = [bob, sue, tom]      #不同的类形成的实例，可以组合在一起
    for obj in db:
        obj.giveraise(0.2)   #Person和Manager类的实例都拥有giveraise这个方法
        print(obj.getlastname(), '=>', obj.pay)
