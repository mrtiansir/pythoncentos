#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

'''
Interface            IP Address      Interface Status
Vlan150              10.159.195.2    protocol-up/link-up/admin-up

   VLAN     MAC Address      Type      age     Secure NTFY Ports
---------+-----------------+--------+---------+------+----+------------------
*  150     7426.aceb.66ff   dynamic  0         F      F    Po100
*  500     0ec9.2e8c.d621   dynamic  0         F      F    Eth1/24
'''
import re
import os


str1 = 'Vlan150              10.159.195.2    protocol-up/link-up/admin-up'
str2 = '*  500     0ec9.2e8c.d621   dynamic  0         F      F    Eth1/24'

str1_result = re.match('(^[a-zA-Z]+\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+([a-z]+-[a-z]+/[a-z]+-[a-z]+/[a-z]+-[a-z]+)', str1).groups()
interface = f'{"接口":<10s}: {str1_result[0]:<40s}'
ip_add = f'{"IP地址":<10s}: {str1_result[1]:<40s}'
int_status = f'{"状态":<10s}: {str1_result[2]:<40s}'
print('-'*80)
print(interface)
print(ip_add)
print(int_status)
print('-'*80)


str2_result = re.match('^\*\s+(\d+)\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+([a-z]{5,})\s+[0-9]\s+[A-Z]\s+[A-Z]\s+(\w+/[0-9]+$)', str2).groups()
vlan_id = f'{"VLAN ID":<15s}: {str2_result[0]:<25s}'
mac = f'{"MAC":<15s}: {str2_result[1]:<25s}'
type = f'{"Type":<15s}: {str2_result[2]:<25s}'
interface = f'{"Interface":<15s}: {str2_result[3]:<25s}'

print('-'*80)
print(vlan_id)
print(mac)
print(type)
print(interface)
print('-'*80)


str3 = os.popen('ifconfig' + ' ens160').read()     #获取对应网卡ifconfig输出信息

str3_result = re.findall('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', str3)
str3_mac = re.findall('([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})', str3)

for i in str3_result:
    if i.split('.')[-1] == '0':
        netmask = i
    elif i.split('.')[-1] == '255':
        network = i
    else:
        ip_addr = i

print(f'{"IP地址":<15s}: {ip_addr:<30s}')
print(f'{"MAC地址":<15s}: {str3_mac[0]:<30s}')
print(f'{"子网掩码":<13s}: {netmask:<30s}')
print(f'{"网络号":<14s}: {network:<30s}')









