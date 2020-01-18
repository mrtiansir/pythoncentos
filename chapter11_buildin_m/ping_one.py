#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from kamene.all import *

def myping():
    ping_pkt = IP(dst=sys.argv[1])/ICMP()
    result = sr1(ping_pkt, timeout=2, verbose=False)
    if result:
        print(sys.argv[1] + ' 通！')
    else:
        print(sys.argv[1] + ' 不通！')

if __name__ == '__main__':
    myping()
