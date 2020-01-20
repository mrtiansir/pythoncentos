#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import ipaddress
net = ipaddress.ip_network('10.159.202.0/24')
# print(type(net))
for x in net:
    print(x)


if __name__ == '__main__':
    pass
    