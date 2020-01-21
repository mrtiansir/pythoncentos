#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import ipaddress

def sort_ip(ips):
    return sorted(ips, key=lambda ip: ipaddress.ip_address(ip))

if __name__ == '__main__':
    ips = ['1.2.3.4', '10.159.202.1', '192.168.1.1', '172.16.10.2', '222.102.134.68', '8.8.8.8']
    print(sort_ip(ips))

    