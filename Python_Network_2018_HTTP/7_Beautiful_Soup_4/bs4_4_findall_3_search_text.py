#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bs4_1_get_soup import taobao_soup
import re
# 通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
print(taobao_soup.find_all(text="淘宝网"))
print(taobao_soup.find_all(text=re.compile("淘宝")))
print(taobao_soup.find_all('a', text=re.compile("淘宝")))
