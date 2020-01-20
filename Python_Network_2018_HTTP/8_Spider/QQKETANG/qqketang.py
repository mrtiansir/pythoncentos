#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from qqketang_page import getpage
from qqketang_getlastpage import getlastpage


def getall(direction):
    # 想获取这个方向的最大页码号
    max_page = getlastpage(direction)
    all_coures = []
    for page in range(max_page):
        # 爬取每一页的内容,并且扩展(extend)到列表all_coures
        all_coures.extend(getpage(direction, page+1))

    return all_coures


if __name__ == '__main__':
    print(getall("ccie"))
