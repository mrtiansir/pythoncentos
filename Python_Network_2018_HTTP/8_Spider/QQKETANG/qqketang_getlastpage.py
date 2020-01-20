#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bs4 import BeautifulSoup
import requests
import re


def getlastpage(direction):
    client = requests.session()
    # 腾讯课堂CCIE课程页面URL
    url = 'https://ke.qq.com/course/list/' + direction

    # 获取腾讯课堂CCIE课程页面
    qqketang = client.get(url)

    # lxml HTML 解析器
    qqketang_soup = BeautifulSoup(qqketang.text, 'lxml')
    # print(qqketang_soup.prettify())
    # 找到所有页码ID的a标签
    allpageid_tag = qqketang_soup.find_all('a', class_=re.compile("^page-btn.*"))
    page_list = []
    for page_id in allpageid_tag:
        try:
            # 提取页码ID,转换为整数后放入page_list列表
            page_list.append(int(page_id.text))
        except Exception as e:
            pass
    # 返回最大的页码号
    return max(page_list)


if __name__ == "__main__":
    print(getlastpage('python'))

