#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

#48-bit MAC to EUI-64 IPv6

import ipaddress
import re

def mac2eui64(mac, prefix=None):
    #将以.:-分隔的mac中的分隔符去掉,以小写输出
    eui64 = re.sub(r'[.:-]', '', mac).lower()
    #mac地址中间加入fffe
    eui64 = eui64[0:6] + 'fffe' + eui64[6:]
    #^是XOR（异或）计算，相同取0，不同取1
    #zfill，返回指定长度的字符串，输出结果右对齐，前面填充0
    #Convert hex to binary(16进制转二进制)：
    # my_hexdata = "1a"
    # scale = 16 ## equals to hexadecimal
    # num_of_bits = 8
    # bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    #hex(int(eui64[0:2], 16) ^ 2)输出结果为0x1111111，取[2:]的内容
    eui64 = hex(int(eui64[0:2], 16) ^ 2)[2:].zfill(2) + eui64[2:]
    if prefix is None:
        return ':'.join(re.findall('.{4}', eui64))     #如果prefix不存在，将eui64以:分隔输出
    else:
        try:
            net = ipaddress.ip_network(prefix, strict=False)
            euil = int(f'0x{eui64}', 16)
            return str(net[euil])
        except:
            return

if __name__ == '__main__':
    print(mac2eui64(mac='68:f7:28:e0:5e:9e', prefix='2002::/64'))

