#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import os
import re
result = os.popen('route -n').read()
# result = '''Kernel IP routing table
# Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
# 10.159.191.128  0.0.0.0         255.255.255.128 U     0      0        0 eth6
# 10.159.98.128   0.0.0.0         255.255.255.128 U     0      0        0 eth5
# 10.159.63.128   0.0.0.0         255.255.255.128 U     0      0        0 eth7
# 10.159.96.0     10.159.98.254   255.255.224.0   UG    0      0        0 eth5
# 10.199.64.0     10.159.63.254   255.255.224.0   UG    0      0        0 eth7
# 10.159.0.0      10.159.63.254   255.255.128.0   UG    0      0        0 eth7
# 10.159.128.0    10.159.191.254  255.255.128.0   UG    0      0        0 eth6
# 10.199.128.0    10.159.191.254  255.255.128.0   UG    0      0        0 eth6
# 10.199.0.0      10.159.63.254   255.255.128.0   UG    0      0        0 eth7
# 169.254.0.0     0.0.0.0         255.255.0.0     U     1002   0        0 eth5
# 169.254.0.0     0.0.0.0         255.255.0.0     U     1003   0        0 eth6
# 169.254.0.0     0.0.0.0         255.255.0.0     U     1004   0        0 eth7
# 192.168.0.0     10.159.63.254   255.255.0.0     UG    0      0        0 eth7
# 10.0.0.0        10.159.63.254   255.0.0.0       UG    0      0        0 eth7
# 0.0.0.0         10.159.191.254  0.0.0.0         UG    0      0        0 eth6'''
list_route = result.split('\n')
f_list_route = []
# print(list_route)
for x in list_route:
    if re.match('^[0-9]{1,3}.*', x):
        gw = re.match('(^[0-9]{1,3}.*)', x).groups()        #筛选出路由表条目，去除列标题等
        f_list_route.append(gw[0])

# print(f_list_route)

list_gw = []

for a in f_list_route:
    f_gw = re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*', a).groups()
    list_gw.append(f_gw[0])

# print(list_gw)
set_gw = set(list_gw)    #去除重复数据
list_gw = list(set_gw)
# print(list_gw)

for b in list_gw:
    last_octer = b.split('.')[3]
    if last_octer != '0':
        print('网关为：' + str(b))


