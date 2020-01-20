#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from kamene.all import *


def my_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    result = sr1(ping_pkt, timeout=30, verbose=False)
    if not result:
        return ip, 2
    elif result[1].type == 0 and result[1].code == 0:
        return ip, 1
    else:
        return ip, 0






if __name__ == '__main__':
    ip = '10.159.202.255'
    result = my_ping(ip)
    print(result)



    