#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from my_python_basic.chapter_13_multi_process.class_13_ssh_client_no_async import ssh_client_no_async
import gevent
from gevent import monkey

monkey.patch_all()

def get_ssh_result(i):
    print('start', i)
    result = ssh_client_no_async('localhost', 22, 'root', 'cisco.123,elk', 'ls / -an', i)
    print('end', i)
    return result

tasks = [gevent.spawn(get_ssh_result, i) for i in range(3)]
all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())




    