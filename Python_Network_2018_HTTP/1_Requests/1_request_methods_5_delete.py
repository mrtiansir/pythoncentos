#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
from requests.auth import HTTPBasicAuth

# 下面两句用于禁止告警信息
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

request_url = 'https://10.1.1.253/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=0'

# 添加认证信息,取消对证书的验证
r = requests.delete(request_url, auth=HTTPBasicAuth('admin', 'Cisc0123'), verify=False)

print(r.status_code)
