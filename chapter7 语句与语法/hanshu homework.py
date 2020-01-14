#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
# def five():
#     num = 5
#     num = num + 1
#
# def main():
#     num = 1
#     five()
#     return num
#
# print(main())


####################################
# def five():
#     global num
#     num = num + 1
#
# def main():
#     global num
#     num = 1
#     five()
#     return num
# print(main())

###################################################
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def my_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt,timeout=2,verbose=False)
    if ping_result:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result = my_ping('10.159.202.254')
    if result == 1:
        print("10.159.202.254 通！")
    if result == 0:
        print("10.159.202.254 不通！")



