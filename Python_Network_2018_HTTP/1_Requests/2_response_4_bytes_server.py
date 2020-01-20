#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import pickle
from io import BytesIO
from socket import *


def Server_PIC(ip, port):
    # 创建TCP Socket, AF_INET为IPv4，SOCK_STREAM为TCP
    sockobj = socket(AF_INET, SOCK_STREAM)
    # 绑定套接字到地址，地址为（host，port）的元组
    sockobj.bind((ip, port))
    # 在拒绝连接前，操作系统可以挂起的最大连接数量，一般配置为5
    sockobj.listen(5)

    while True:  # 一直接受请求，直到ctl+c终止程序
        # 接受TCP连接，并且返回（conn,address）的元组，conn为新的套接字对象，可以用来接收和发送数据，address是连接客户端的地址
        connection, address = sockobj.accept()
        # 打印连接客户端的IP地址
        print('Server Connected by', address)
        # 读取客户端数据,测试结果为这个操作为必须
        data = connection.recv(1024)
        dict = {'key1': 'welcome to qytang', 'key2': [1, 2, 3, 4, 5], 'key3': ([3, 4], 'python')}
        # 必须添加Headers,否则requests模块会出现校验头部失败
        header = b'HTTP/1.1 200 OK\nDate: Wed, 05 Sep 2018 09:16:28 GMT\nServer: Apache\n\n'
        # 把字典pickle为字节流
        msg = pickle.dumps(dict)
        # 把字典pickle后的字节流,放在头部后面,
        # 如果没有HTTP的头部,requests会出错
        connection.send(header + msg)
        connection.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    Server_IP = '0.0.0.0'
    Server_Port = 80
    Server_PIC(Server_IP, Server_Port)
