#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
# func(*a) 把可迭代对象a传入函数f，函数根据顺序把对象指派给函数多个本地变量
# func(**a) 把字典传入函数，函数根据映射关系把对象指派给函数多个本地变量

a = [(1, 2, 3, 4, 5, 6), [1, 2, 3, 4, 5], {'a': 1, 'b': 2, 'c': 3}]

dict = {'a':1, 'b':2, 'c':3}

def f(a,b,c):
    print(a,b,c)


if __name__ == '__main__':
    f(*a)
    f(**dict)



