#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import gevent
from gevent import monkey
monkey.patch_all()    # 在import requests之前，需要先给money打补丁，详情参见https://github.com/gevent/gevent/issues/1016  在已导入ssl之后，用猴子修补ssl可能会导致错误，包括Python 3.6上的RecursionError。 它也可能无提示地导致Python 3.7上的错误行为。 请提早给猴子打补丁

import requests

def get_body(i):
    print('start', i)
    result = requests.get('https://www.sina.com.cn')
    print('end', i)
    return result

tasks = []
for i in range(3):
#   task = gevent.spawn(get_body, i)
    tasks.append(gevent.spawn(get_body, i))

# tasks = [gevent.spawn(get_body, i) for i in range(3)]           #三元表达式写法

result = gevent.joinall(tasks)    #等待所有task执行完毕

for x in result:
    print(x.get())
    # print(x.get().text)





    