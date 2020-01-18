#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import paramiko

def ssh_client(ip, username, password, port, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, port=port, timeout=10, compress=True)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        ssh.close()
        return x
    except Exception as e:
        # pass
        print(f'{ip} 连接失败！ {e}')



if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'usag:python simple_ssh_client.py -i ipaddr -u username -p password -o port -c command'

    parser = ArgumentParser(usage=usage)

    parser.add_argument('-i', '--ipaddr', dest='ip', help='SSH Server', default='10.159.202.254', type=str)
    parser.add_argument('-u', '--username', dest='username', help='SSH Username', default='root', type=str)
    parser.add_argument('-p', '--password', dest='password', help='SSH Password', type=str)
    parser.add_argument('-o', '--port', dest='port', help='SSH Port', type=str)
    parser.add_argument('-c', '--command', dest='cmd', help='Shell Command', default='ls', type=str)

    args = parser.parse_args()

    print(ssh_client(args.ip, args.username, args.password, args.port, args.cmd))
    