#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://www.qytpython.com/http_basic_authen.php', auth=HTTPBasicAuth('user', 'pass'))

print(r.text)
