#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from kamene.all import *

class myping:
    def __init__(self,ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def src(self,srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)


    def size(self,length):
        self.length = length
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def one(self):
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip + "可达！")
        else:
            print(self.ip + "不可达！")

    def ping(self):
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.srcip:
            return f'<dstip: {self.ip}, size: {self.length}>'
        else:
            return f'<srcip: {self.srcip}, dstip: {self.ip}, size: {self.length}>'


if __name__ == '__main__':
    ping_test = myping('10.159.202.254')
    # print(ping_test)
    ping_test.one()
    ping_test.ping()
    ping_test.size(200)
    # print(ping_test)
    ping_test.src('10.159.202.219')
    # print(ping_test)
    ping_test.ping()
