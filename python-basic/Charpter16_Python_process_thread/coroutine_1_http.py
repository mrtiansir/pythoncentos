#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# https://thief.one/2017/02/20/Python协程/


import gevent
from gevent import monkey

monkey.patch_all()
import requests


def get_body(i):
    print("start", i)
    result = requests.get("http://www.qytang.com")
    print("end", i)
    return result


tasks = [gevent.spawn(get_body, i) for i in range(3)]
all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())
    # print(x.get().text)

