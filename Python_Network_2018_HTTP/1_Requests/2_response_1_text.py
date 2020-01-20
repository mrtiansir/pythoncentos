#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

# 请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。当你访问 r.text 之时，
# Requests 会使用其推测的文本编码。你可以找出 Requests 使用了什么编码，
# 并且能够使用 r.encoding 属性来改变它：
r = requests.get('http://www.qytpython.com')

print(r.text)
print(r.encoding)  # UTF-8

r = requests.get('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv140&productId=20045127777&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')

# r.encoding = 'GB18030'  # 解码正常
# r.encoding = 'UTF-8'  # 解码出现问题
print(r.text)
print(r.encoding)  # 这个页面默认选择的解码为GBK

