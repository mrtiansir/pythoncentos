#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
#
# r = requests.get('http://www.qytpython.com/cgi-bin/testcgi.py', params={'user': 'cq_bomb', 'age': '39'})
#
# print(r.text)


# r = requests.post('http://www.qytpython.com/cgi-bin/testcgi.py', data={'user': 'cq_bomb', 'age': '39'})
#
# print(r.text)

r = requests.get('http://10.1.1.100/data', params={'key1': 'value1', 'key2': 'value2'})

print(r.text)

r = requests.post('http://10.1.1.100/data', data=(('key1', 'value1'), ('key2', 'value2')))

print(r.text)
