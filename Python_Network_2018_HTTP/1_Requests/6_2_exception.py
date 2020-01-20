#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

# 主动抛出异常,然后用except捕获
try:
    r = requests.get('http://www.qytang.com/%qytang')
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)

# 产生超时异常,捕获并且打印信息
try:
    r = requests.get('http://www.qytang.com', timeout=0.001)
except requests.exceptions.ConnectTimeout:
    print('请求超时')




