#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import os
import time


while True:
    monitor_result = os.popen('netstat -nlupt | grep :80').read()
    # monitor_list = monitor_result.split()
    # port_status = monitor_list[3].split(':')[-1]
    if monitor_result == '':
        print('HTTP TCP/80已停止运行！')
        break
    # if monitor_result != '':
    #     print('HTTP TCP/80运行正常，等待5S后再进行检测')
    #     time.sleep(5)
    else:
        print('HTTP TCP/80运行正常，等待5S后再进行检测')
        time.sleep(5)



