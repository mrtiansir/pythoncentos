#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import re

str = '''TCP cnc  101.71.30.49:6810 jiankong  192.168.100.62:46421, idle 0:00:28, bytes 54929844, flags UxIO 
TCP cnc  101.71.30.190:6810 jiankong  192.168.100.66:58441, idle 0:00:25, bytes 10423768, flags UxIO 
TCP cnc  101.71.30.190:6820 NVR  192.168.240.2:53684, idle 0:00:04, bytes 98375209, flags UxIO 
TCP cnc  101.71.30.191:6806 jiankong  192.168.100.61:46593, idle 0:00:07, bytes 31711904, flags UxIO 
TCP cnc  101.71.30.192:6810 jiankong  192.168.100.63:34587, idle 0:00:10, bytes 5370656, flags UxIO 
TCP cnc  101.71.4.135:6808 jiankong  192.168.100.64:42712, idle 0:00:28, bytes 20339360, flags UxIO 
TCP cnc  101.71.4.135:6806 jiankong  192.168.100.65:43674, idle 0:00:08, bytes 99677232, flags UxIO 
TCP cnc  101.71.30.206:6804 jiankong  192.168.100.67:54024, idle 0:00:21, bytes 29017881, flags UxIO 
TCP cnc  101.71.4.146:6808 jiankong  192.168.100.69:44250, idle 0:00:06, bytes 38961359, flags UxIO 
TCP cnc  101.71.4.144:6804 jiankong  192.168.100.68:55509, idle 0:00:28, bytes 99694236, flags UxIO'''

list1 = str.split('\n')
# print(list1)

dict1 = {}

for x in list1:
    result = re.match('(^[A-Z]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+),\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+([0-9]+),\s+flags\s+(\w+)', x).groups()
    # print(result)
    conn_key = result[1], result[2], result[3], result[4]
    # print(conn_key)
    conn_value = result[5], result[6]
    # print(conn_value)
    dict1[conn_key] = conn_value

print('\n\n打印字典\n')
print(dict1)

print("\n打印格式化输出\n")

for key, value in dict1.items():
    print(f'{"src":>10s} : {key[0]:<20s}|{"src_p":>10s} : {key[1]:<10s}|{"dst":>10s} : {key[2]:<20s}|{"dst_p":>10s} : {key[3]:<10s}|')
    print(f'{"bytes":>10s} : {value[0]:<20s}|{"flags":>10s} : {value[1]:<20s}')
    print('='*116)




