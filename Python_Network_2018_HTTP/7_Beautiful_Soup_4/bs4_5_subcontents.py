#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bs4_1_get_soup import taobao_soup
import bs4
import re

# 访问直接子节点
# 找到页面里边的产品清单
# print(taobao_soup.find('div', id="J_ItemList"))

# 你会发现'\n'(换行)会出现在直接子节点里边
# print(taobao_soup.find('div', id="J_ItemList").contents)

# 由于'\n'(换行)会出现在直接子节点里边!所以要排除错误可能
# for item in taobao_soup.find('div', id="J_ItemList").contents:
#     try:
#         print('产品ID: ', item.get('data-id'))
#     except AttributeError as e:
#         pass

# for item in taobao_soup.find('div', id="J_ItemList").contents:
#     try:
#         if type(item.find(class_="productImg-wrap").find('img')) is bs4.element.Tag:
#             print(item.find(class_="productImg-wrap").find('img'))  # 找到的仅仅是大图
#     except Exception as e:  # 排除'\n'
#         pass


# 访问所有子孙节点
# for subitem in taobao_soup.find('div', id="J_ItemList").descendants:
#     try:
#         if type(subitem.find('img')) is bs4.element.Tag:  # 找到所有的图,包括缩图
#             print(subitem.find('img'))
#     except Exception as e:  # 排除'\n'
#         pass


# -------------------------------------------------------------------------------------

# 换一下思路
# 找到所有产品ID
# def has_class_and_data_id(tag):
#     return tag.has_attr('class') and tag.has_attr('data-id') and tag.has_attr('data-atp')
#
#
# for a in taobao_soup.find_all(has_class_and_data_id):
#     print(a.attrs.get('data-id'))

# 找到所有的大图
# for largeimg in taobao_soup.find_all('a', class_="productImg"):
#     # print(largeimg.find('img'))
#     for key, value in largeimg.find('img').attrs.items():
#         if re.match('src|^data-ks-lazyload.*', key):
#             print('URL: http:' + value)

# 找到所有的缩图
# for minimg in taobao_soup.find_all('b', class_="proThumb-img"):
#     # print(minimg.find('img'))
#     for key ,value in minimg.find('img').attrs.items():
#         if key.startswith('data-ks-lazyload'):
#             print('URL: http:' + value)

# 找到所有价格
# for price in taobao_soup.find_all('p', class_="productPrice"):
#     print(price.text.strip())
