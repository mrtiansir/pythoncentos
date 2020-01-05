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


str3 = '''
ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.159.202.219  netmask 255.255.255.0  broadcast 10.159.202.255
        inet6 fe80::95f0:65d3:4b1a:9a67  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:b2:56:84  txqueuelen 1000  (Ethernet)
        RX packets 26322441  bytes 5641045270 (5.2 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 631173  bytes 92429652 (88.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
'''

str3_result = re.findall('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', str3)
ip_addr = f'{"IP地址":<15s}: {str3_result[0]:<30s}'
netmask = f'{"子网掩码":<13s}: {str3_result[1]:<30s}'
network = f'{"网络号":<14s}: {str3_result[2]:<30s}'
print(ip_addr)
print(netmask)
print(network)





