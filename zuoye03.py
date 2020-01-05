#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import re

str1 = 'TCP outside  52.114.158.92:443 inside  192.168.223.4:26868, idle 0:01:19, bytes 9887, flags UxIO'
str2 = 'TCP outside  52.114.158.92:443 inside  192.168.223.4:26867, idle 0:01:17, bytes 9693, flags UxIO'
str3 = 'TCP outside  180.87.4.141:443 inside  192.168.10.18:49217, idle 0:00:28, bytes 3324, flags UfFRxIO'

str1_key = re.match('(^[A-Z]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+),\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+[0-9]+,\s+flags\s+[a-zA-Z]+', str1).groups()
str1_value = re.match('^[A-Z]+\s+[a-zA-Z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+\s+[a-zA-Z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+,\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+([0-9]+),\s+flags\s+([a-zA-Z]+)', str1).groups()
# print(str1_key)
# print(str1_value)
str2_key = re.match('(^[A-Z]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+),\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+[0-9]+,\s+flags\s+[a-zA-Z]+', str2).groups()
str2_value = re.match('^[A-Z]+\s+[a-zA-Z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+\s+[a-zA-Z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+,\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+([0-9]+),\s+flags\s+([a-zA-Z]+)', str2).groups()
str3_key = re.match('(^[A-Z]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+)\s+[a-zA-Z]+\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+),\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+[0-9]+,\s+flags\s+[a-zA-Z]+', str3).groups()
str3_value = re.match('^[A-Z]+\s+[a-zA-Z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+\s+[a-zA-Z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+,\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+([0-9]+),\s+flags\s+([a-zA-Z]+)', str3).groups()

list1 = []
list2 = []
list1.append(str1_key)
list1.append(str2_key)
list1.append(str3_key)
# print(list1)

list2.append(str1_value)
list2.append(str2_value)
list2.append(str3_value)
# print(list2)

dic_conn = dict(zip(list1, list2))
# print(dic_conn)

print(f'{"src":>10s} : {str1_key[1]:<20s}|{"src_p":>10s} : {str1_key[2]:<10s}|{"dst":>10s} : {str1_key[3]:<20s}|{"dst_p":>10s} : {str1_key[4]:<10s}|')
print(f'{"bytes":>10s} : {str1_value[0]:<20s}|{"flags":>10s} : {str1_value[1]:<20s}')
print('='*120)
print(f'{"src":>10s} : {str2_key[1]:<20s}|{"src_p":>10s} : {str2_key[2]:<10s}|{"dst":>10s} : {str2_key[3]:<20s}|{"dst_p":>10s} : {str2_key[4]:<10s}|')
print(f'{"bytes":>10s} : {str2_value[0]:<20s}|{"flags":>10s} : {str2_value[1]:<20s}')
print('='*120)
print(f'{"src":>10s} : {str3_key[1]:<20s}|{"src_p":>10s} : {str3_key[2]:<10s}|{"dst":>10s} : {str3_key[3]:<20s}|{"dst_p":>10s} : {str3_key[4]:<10s}|')
print(f'{"bytes":>10s} : {str3_value[0]:<20s}|{"flags":>10s} : {str3_value[1]:<20s}')
print('='*120)



