#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import requests
from bs4 import BeautifulSoup


client = requests.session()


def findImages(url):
    print('发现在URL上的图片文件: ' + url)
    urlContent = client.get(url)
    soup = BeautifulSoup(urlContent.text, "lxml")
    # 找到所有的img(图片)标签
    tags = soup.find_all('img')

    imgnames = []
    for tag in tags:
        # 提取img(图片)标签中的src属性(相对路径,本页面仅仅只是图片的名字),并且放入列表imgnames
        # <img src="gps_test_1.jpg" height="100" width="100" />
        imgnames.append(tag['src'])
    # print(url.split('/'))
    # ['http:', '', 'webtest.qytang.com', 'gps', 'gps.html']
    # [2:-1] = ['webtest.qytang.com', 'gps']
    # '/'.join(url.split('/')[2:-1]) = 'webtest.qytang.com/gps'
    prefix = 'http://' + '/'.join(url.split('/')[2:-1]) + '/'
    # 上面代码得到的结果为'http://webtest.qytang.com/gps/'

    img_urls = []

    for imgname in imgnames:
        # 把前缀与文件名进行拼接,得到后续下载图片用的完整链接,并且把完整链接放入列表img_urls
        img_urls.append(prefix + imgname)
    # 返回拥有所有图片完整链接的列表
    return img_urls


if __name__ == '__main__':
    print(findImages('http://webtest.qytang.com/gps/gps.html'))
