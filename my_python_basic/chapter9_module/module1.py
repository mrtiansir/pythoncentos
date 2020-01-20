#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
import paramiko

def my_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return 1
    else:
        return 0

def my_ssh(ip, port, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, port=port, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        ssh.close()
        return x
    except Exception as e:
        print(f'{ip} 连接失败！{e}')



if __name__ == '__main__':
    hosts = ['10.159.202.219', '10.159.202.218', '10.159.202.217']
    for ip in hosts:
        if my_ping(ip) == 1:
            print(ip + ' 可达！')
            cmd = 'ifconfig'
            ssh_result = my_ssh(ip, 22, 'root', 'cisco.123,elk', cmd)
            print('登录 ' + ip + ' 执行命令 ' + cmd + ' 回显结果如下：')
            print(ssh_result)
            print('='*60)
        else:
            print(ip + ' 不通！')

    