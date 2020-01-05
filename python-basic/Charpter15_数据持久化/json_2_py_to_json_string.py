#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import json
from source_db import qyt_teachers# 导入字典

print(qyt_teachers)  # 打印字典
print(type(qyt_teachers))

json_string = json.dumps(qyt_teachers, ensure_ascii=False)
print(json_string)
print(type(json_string))

dict_recv = json.loads(json_string)
print(dict_recv)
print(type(dict_recv))



