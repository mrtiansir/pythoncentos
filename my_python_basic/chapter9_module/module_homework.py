#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts


from my_python_basic.chapter9_module.module1 import my_ping, my_ssh

prefix = '10.159.202.'

for host in range(1,255):
    ip = prefix + str(host)
    if my_ping(ip) == 1:
        print(ip + ' 可达！')
        cmd = 'ifconfig'
        cmd_result = my_ssh(ip, 22, 'root', 'cisco.123,elk', cmd)
        print('登录 ' + ip + ' 执行命令 ' + cmd + ' 回显结果如下：')
        print(cmd_result)
        print('='*60)
    else:
        print(ip + ' 不通！')
        print('='*60)




if __name__ == '__main__':
    pass
    