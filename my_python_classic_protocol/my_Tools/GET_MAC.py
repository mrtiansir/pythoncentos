#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import netifaces
import platform


def GET_MAC(ifname):
    if platform.system() == 'Linux':
        return netifaces.ifaddresses(ifname)[netifaces.AF_LINK][0]['addr']

    elif platform.system() == 'Windows':
        from my_python_classic_protocol.my_Tools.WIN_GET_IFACE_ID import win_from_ifname_getid
        if_id = win_from_ifname_getid(ifname)
        return netifaces.ifaddresses(if_id)[netifaces.AF_LINK][0]['addr']

    else:
        print('操作系统不支持，本脚本只能工作在Linux或Windows平台！')

if __name__ == '__main__':
    print(GET_MAC('pc'))
    