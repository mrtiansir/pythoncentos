#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
import platform

def get_ip_address(ifname):
    if platform.system() == 'Linux':
        return ifaddresses(ifname)[AF_INET][0]['addr']

    elif platform.system() == 'Windows':
        from my_python_classic_protocol.my_Tools.WIN_GET_IFACE_ID import win_from_ifname_getid
        if_id = win_from_ifname_getid(ifname)
        return ifaddresses(if_id)[AF_INET][0]['addr']

    else:
        print('操作系统不支持，本脚本只能工作在Linux或者Windwos平台！')

def get_ipv6_address(ifname):
    if platform.system() == 'Linux':
        return ifaddresses(ifname)[AF_INET6][0]['addr']

    if platform.system() == 'Windows':
        from my_python_classic_protocol.my_Tools.WIN_GET_IFACE_ID import win_from_ifname_getid
        if_id = win_from_ifname_getid(ifname)
        return ifaddresses(if_id)[AF_INET6][0]['addr']

    else:
        print('操作系统不支持，本脚本只能运行在Linux或Windows平台！')


if __name__ == '__main__':
    print(get_ip_address('pc'))
    print(get_ipv6_address('pc'))

    