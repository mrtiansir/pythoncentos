#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from bs4_1_get_soup import taobao_soup


# 只找到的第一个a标签,的全部内容
print(taobao_soup.a)
print("-"*100)

# 名字为"a"
print(taobao_soup.a.name)
print("-"*100)

# 提取a标签的全部属性值,产生为字典
# {'href': '//login.taobao.com/member/login.jhtml?f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F', 'target': '_top'}
print(taobao_soup.a.attrs)
print("-"*100)

# 提取attrs href
print(taobao_soup.a['href'])
print("-"*100)

# 提取attrs target
print(taobao_soup.a['target'])
print("-"*100)

# 提取标签a内的文本
print(taobao_soup.a.text)
