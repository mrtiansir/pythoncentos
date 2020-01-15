#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
# *args 把传进来的内容转换为元组，赋值给args，传进来的值格式为'1,2,3,4,5,6,[1,2,3,4,5,6],{'a':1, 'b':2, 'c':3}
# **kwargs 把传进来的内容转换为字典，赋值给kwargs，传进来的值格式为'a=1, b=2, c=3'
def printer(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    printer(1,2,3,4,5,6,6,8,[1,2,3,4,5,6,7],a=1, b=2, c=3)
    