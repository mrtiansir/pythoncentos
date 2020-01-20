#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import paramiko

def my_ssh(ip, username, password, port=22, cmd='ifconfig'):
    ssh =  paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,username=username,password=password,port=port,timeout=10,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    ssh.close()
    return x

if __name__ == '__main__':
    # print(my_ssh('10.159.202.219', 'root', 'cisco.123,elk',))
    print(my_ssh('10.159.202.219', 'root', 'cisco.123,elk',cmd='ls'))


