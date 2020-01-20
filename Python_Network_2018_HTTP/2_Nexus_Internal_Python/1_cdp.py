#!/usr/bin/python
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cli import *
from cisco.interface import *
import json
import re


def getupintlist():
    # 查看接口摘要
    intflist = json.loads(clid('show interface brief'))
    i = 0
    upintflist = []
    # 通过while循环找到那些状态处于up的以太网接口
    while i < len(intflist['TABLE_interface']['ROW_interface']):
        intf = intflist['TABLE_interface']['ROW_interface'][i]
        i = i + 1
        if intf['state'] == 'up':
            if re.match('.*Ether.*', intf['interface']):
                # 把状态处于up的以太网接口的名字放入upintflist清单
                upintflist.append(intf['interface'])
    # 返回状态处于up的以太网接口名字的清单upintflist
    return upintflist


def getneiname(ifname):
    try:
        # 查询特定接口的CDP邻居信息
        neidetail = json.loads(clid('show cdp neighbors interface %s' % ifname))
        # 提取CDP邻居的device_id信息,并返回
        return neidetail['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']['device_id']
    except:
        return None


def config_description(ifname):
    # 产生接口实例
    if_config = Interface(ifname)
    # 配置接口描述
    if_config.set_description('description link to %s' % getneiname(ifname))


if __name__ == '__main__':
    # print getupintlist()
    # print(getneiname('ethernet1/3'))
    # config_description('ethernet1/1')

    up_interfaces = getupintlist()
    for x in up_interfaces:
        if getneiname(x):
            config_description(x)
