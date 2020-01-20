#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# 参考文档 https://cuiqingcai.com/1319.html

from bs4_1_get_soup import taobao_soup
import bs4
print(taobao_soup.title)
print("-"*100)
print(taobao_soup.head)
print("-"*100)
# 这种方式,只找到第一个符合要求的标签a
print(taobao_soup.a)
print("-"*100)
# 这种方式,只找到第一个符合要求的标签p
print(taobao_soup.p)
print("-"*100)
# 类型为<class 'bs4.element.Tag'>
print(type(taobao_soup.p))
if type(taobao_soup.p) is bs4.element.Tag:
    print('match!')
