#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from kamene.all import *
from my_python_classic_protocol.my_Tools.GET_IP import get_ip_address
from my_python_classic_protocol.my_Tools.GET_MAC import GET_MAC
from my_python_classic_protocol.my_Tools.GET_IFACE_NAME import get_ifname

def arp_request(ip_address, ifname='ens160'):
    #获取本机ip地址
    localip = get_ip_address(ifname)
    #获取本机MAC地址
    localmac = GET_MAC(ifname)
    try:
        result_raw = sr1(ARP(op=1,
                             hwsrc=localmac,
                             hwdst='00:00:00:00:00:00',
                             psrc=localip,
                             pdst=ip_address), iface=get_ifname(ifname), timeout=1, verbose=False)
        return ip_address, result_raw.getlayer(ARP).fields.get('hwsrc')
    except AttributeError:
        return ip_address, None

if __name__ == '__main__':
    arp_result = arp_request('10.159.202.254', 'ens160')
    print(f'IP地址：{arp_result[0]}, MAC地址：{arp_result[1]}')

    