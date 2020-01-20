#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

# 京东由于数字证书有效,所以直接可以得到结果
# r = requests.get('https://www.jd.com')
#
# print(r.text)

# 任务一:禁止告警信息
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# www.qytpython.com为自签名证书
# 任务二:使用verify=False略过证书检查
r = requests.get('https://www.qytpython.com', verify=False)

print(r.text)
