#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cisco.interface import *
from nxos import *

"""
周期性调度:
feature scheduler 
scheduler job name run_python
    python bootflash:///3_monitor_if.py
    exit
scheduler schedule name schedule_run_python
    job name run_python
    time start now repeat 0:0:1
    end
    
查看日志:
NXOS1# show logging logfile 
2018 Sep  8 01:07:02 NXOS1  %USER-3-SYSTEM_MSG: Interface state is up! - nxpython
2018 Sep  8 01:12:07 NXOS1  %USER-3-SYSTEM_MSG: Interface state is up! - nxpython
2018 Sep  8 01:14:11 NXOS1  %USER-3-SYSTEM_MSG: Interface state is down!, try to no shutdown! - nxpython
"""
# 产生接口实例
lo0 = Interface('loopback0')
# 判断接口是否Down
if lo0.show().admin_state == 'down':
    # 如果接口处于down的状态,就重新打开接口,并且产生系统日志
    lo0.set_state(s="up")
    py_syslog(3, 'Interface state is down!, try to no shutdown!')
else:  # 如果接口处理up状态,依然产生正常的系统日志
    py_syslog(3, 'Interface state is up!')
