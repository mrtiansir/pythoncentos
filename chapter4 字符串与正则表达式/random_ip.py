#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import random #导入random模块

a = random.randint(1,255)   #在1-255之间随机产生整数
b = random.randint(0,255)
c = random.randint(0,255)
d = random.randint(1,255)

ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)

print(ip)


