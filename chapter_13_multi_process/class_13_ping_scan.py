#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

from chapter_13_multi_process.class_13_ping_one import my_ping
from multiprocessing.pool import ThreadPool
import ipaddress

def ping_scan(network):
    pool = ThreadPool(processes=150)
    net = ipaddress.ip_network(network)

    result_obj_dict = {}

    for ip in net:
        result_obj = pool.apply_async(my_ping, args=(str(ip),))
        result_obj_dict[str(ip)] = result_obj

    pool.close()
    pool.join()

    active_ip = []

    for ip, obj in result_obj_dict.items():
        if obj.get()[1] == 1:
            active_ip.append(ip)

    return active_ip

if __name__ == '__main__':
    import pickle
    from datetime import datetime
    filename = 'scan_save_pickle_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.pl'
    dbfile = open(filename, 'wb')
    scan_net = input('请输入需要扫描的网段，eg. 192.168.1.0/24：')
    print('请稍等，ping扫描正在进行中......')
    result = ping_scan(scan_net)
    pickle.dump(result, dbfile)
    dbfile.close()
    dbfile = open(filename, 'rb')
    final = pickle.load(dbfile)
    print(f'扫描完毕，网段{scan_net}中活动ip如下：')
    print('='*60)
    for final_ip in final:
        print(final_ip)
















