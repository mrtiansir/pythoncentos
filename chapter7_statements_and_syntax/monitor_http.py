#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import os
import time

while True:
    httpd_result = os.popen('netstat -nlupt').read()
    monitor_list = httpd_result.split('\n')
    monitor_list = monitor_list[2:-1]

    for x in monitor_list:
        if x.split()[3].split(':')[-1] == '80':
            print('HTTP (TCP/80)服务已经被打开')
            break
        else:
            print('等待5S重新开始监控！')
            time.sleep(5)
            continue
    break
