#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bs4_1_get_soup import taobao_soup
import re

# find_all( name , attrs , recursive , text , **kwargs )
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
# 注意：如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性

# 一号方案,传方法, 这种方法可以用于判断是否有相应的属性
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id') and not tag.has_attr('href')
#
#
# for a in taobao_soup.find_all(has_class_but_no_id):
#     print(a.attrs)


# 二号方案: 基于属性的名字, 多个属性的时候可以使用字典
# 严重注意class需要使用class_!!!
# print(taobao_soup.find_all(class_="product"))
# print(taobao_soup.find_all('div', class_="product"))
# print(taobao_soup.find_all('a', class_="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev", title="上一页"))
# print(taobao_soup.find_all('div', attrs={"class": "product", "data-id": "577105132566"}))
for price in taobao_soup.find_all('p', class_="productPrice"):
    print(price.text.strip())


# 三号方案: 基于属性的正则表达式匹配
# print(taobao_soup.find_all('a', href=re.compile("tmall")))
# print(len(taobao_soup.find_all('a', href=re.compile("tmall"))))
# 可以同时对多个属性进行正则表达式匹配
# print(taobao_soup.find_all(href=re.compile("tmall"), rel=re.compile("dns")))


# 有些tag属性在搜索不能使用,例如HTML5中的data-*属性
# data-name="search"
# print(taobao_soup.find_all(data-name="search")) 报错SyntaxError: keyword can't be an expression
# 需要使用如下方式来查找data-*属性
# print(taobao_soup.find_all('div', attrs={"class": "product", "data-id": "577105132566"}))
