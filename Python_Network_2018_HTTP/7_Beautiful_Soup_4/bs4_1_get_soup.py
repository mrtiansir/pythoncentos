#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# 参考文档 https://cuiqingcai.com/1319.html

from bs4 import BeautifulSoup
import requests
from readheader import readheaders


client = requests.session()
# 获取天猫搜索iwatch4页面
url = 'https://list.tmall.com/search_product.htm?q=iwatch4'

# 使用自定义头部信息,通过认证!然后获取天猫搜索iwatch4页面
taobao_home = client.get(url, headers=readheaders('http_header.txt'))

# lxml HTML 解析器
taobao_soup = BeautifulSoup(taobao_home.text, 'lxml')

# 格式化打印BeautifulSoup对象
# print(taobao_soup.prettify())



