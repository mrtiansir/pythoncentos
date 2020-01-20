#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
from urllib.parse import urlsplit
from os.path import basename
import os

client = requests.session()


def downloadImage(imgurls, folder):
    imgFileNames = []
    # 切换到下载文件存放的目录
    os.chdir(folder)
    print('开始下载文件....')
    for imgurl in imgurls:
        # 逐个得到下载文件的完整链接
        try:
            # 获取图片二进制内容
            imgContent = client.get(imgurl).content
            # print(urlsplit(imgurl))
            # SplitResult(scheme='http', netloc='www.qytang.com', path='/gps/gg_gps.jpg', query='', fragment='')
            # urlsplit(imgurl)[2] = '/gps/gg_gps.jpg'
            # basename(urlsplit(imgurl)[2]) = 'gg_gps.jpg'
            imageFileName = basename(urlsplit(imgurl)[2])  # 得到文件名
            imageFile = open(imageFileName, 'wb')
            imageFile.write(imgContent)  # 写入文件内容
            imageFile.close()
            # 产生存放文件的完整路径(目录+文件名),便于后续分析GPS信息的代码读取文件
            imgFileName = str(folder) + str(imageFileName)
            imgFileNames.append(imgFileName)  # 把写入的完整文件路径添加到清单imgFileNames

        except Exception as e:
            print(e)
            pass
    return imgFileNames


if __name__ == '__main__':
    img_urls = ['http://webtest.qytang.com/gps/gg_gps.jpg']
    print(downloadImage(img_urls, "C:\\Users\\Administrator\\PycharmProjects\\Python_Network_2018_HTTP\\8_Spider\\Photo_Spider\\Download_IMG\\"))
