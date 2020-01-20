#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import paramiko

def ssh_client_no_async(ip, port, username, password, cmd, async_id):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        ssh.close()
        return x
    except Exception as e:
        print(f'{ip} 连接失败! {e}')


if __name__ == '__main__':
    print(ssh_client_no_async('10.159.202.219', 22, 'root', 'cisco.123,elk', 'ifconfig', 1))
    