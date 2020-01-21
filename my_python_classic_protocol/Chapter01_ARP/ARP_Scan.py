#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)   #清除报错
from my_python_classic_protocol.Chapter01_ARP.ARP_Request import arp_request
from multiprocessing.pool import ThreadPool
from kamene.all import *


def kamene_arp_scan(network, ifname):
    net = ipaddress.ip_network(network)
    ip_list = []
    for ip_add in net:
        ip_list.append(str(ip_add))   #把IP地址放入ip_list的清单
    pool = ThreadPool(processes=100)
    result = []    #创建清单，放入后续的Thread
    for i in ip_list:
        result.append(pool.apply_async(arp_request, args=(i, ifname)))   #关联函数与参数，并且添加结果到result
    pool.close()  #关闭pool,不再加入新的进程
    pool.join()   #等待每一个进程结束

    scan_dict = {}    #扫描结果IP地址的字典
    for r in result:
        if r.get()[1]:    #如果没有获得MAC地址，就continue进入下一次循环，arp_request中定义如果没有响应，return NONE
            scan_dict[r.get()[0]] = r.get()[1]  #如果获得MAC，将IP/MAC地址放入字典
    return scan_dict


if __name__ == '__main__':
    import time
    t1 = time.time()
    print('开始扫描，请稍等......')
    scan_result = kamene_arp_scan('10.159.202.0/24', 'ens160')
    print('本次扫描，活动ip地址如下：')
    for ip, mac in scan_result.items():
        print(f'IP地址：{ip}, MAC地址：{mac}')
    t2 = time.time()
    print(f'本次扫描耗时：{t2 - t1:<.2f} S')


    