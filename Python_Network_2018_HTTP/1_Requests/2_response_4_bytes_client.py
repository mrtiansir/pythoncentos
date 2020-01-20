#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
import pickle

# stream=True读取字节流数据
r = requests.get('http://10.1.1.100', stream=True)

# 读取原始字节流数据
raw_data = r.raw.read()
print(raw_data)
# 把原始字节流数据使用pickle转换为Python对象
dict = pickle.loads(raw_data)
print(dict)
