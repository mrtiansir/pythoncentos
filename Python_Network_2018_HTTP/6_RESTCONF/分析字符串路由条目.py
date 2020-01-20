#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import re

str1 = """
sdfsdfsdfwer
sdfsdfsdfsdf
sdfsdfsdf
ip route 192.168.1.0 255.255.255.0 10.0.0.1
ip route 192.168.2.0 255.255.255.0 10.0.0.2
sdfsadfasdf
asdfasdfasdf
"""


def parser_route():
    for route in str1.split('\n'):
        if re.match('ip route (\d{1,3}\.){3}\d{1,3} (\d{1,3}\.){3}\d{1,3} (\d{1,3}\.){3}\d{1,3}.*', route):
            result = re.match('ip route ((\d{1,3}\.){3}\d{1,3}) ((\d{1,3}\.){3}\d{1,3}) ((\d{1,3}\.){3}\d{1,3}).*', route.rstrip()).groups()
            dest_net = result[0]
            mask = result[2]
            next_hop = result[4]
            print('目的: %s 掩码: %s 下一跳: %s' % (dest_net, mask, next_hop))


if __name__ == '__main__':
    parser_route()
