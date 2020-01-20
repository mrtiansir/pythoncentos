#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import time
import os
import threading   #引入线程模块

def sum_multi(x, y, z):
    #打印进程和线程ID
#    print('pid tid ==>', os.getpid(),threading.currentThread().ident)
    i = 1
    sum_x_y_z = 0
    while i < 10:
        sum_x_y_z = x * y * z
        x += 1
        y += 1
        z += 1
        i += 1
        time.sleep(1)
    #返回计算结果，进程号，线程号
    return sum_x_y_z, os.getpid(), threading.currentThread().ident



if __name__ == '__main__':
    print(sum_multi(1,2,3))

    