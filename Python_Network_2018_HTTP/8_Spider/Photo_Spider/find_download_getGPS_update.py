#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from find_image_from_www_site_update import findImages
from download_image_from_www_site_update import downloadImage
from find_image_GPS import FindGPSimage
from os.path import basename


def download_findGPS(url):
    imgurls = findImages(url)  # 找到图片文件链接！
    print(imgurls)
    imgFileNames = downloadImage(imgurls, "C:\\Users\\Administrator\\PycharmProjects\\Python_Network_2018_HTTP\\8_Spider\\Photo_Spider\\Download_IMG\\")
    # 下载文件，并且返回文件清单！
    for img_downloaded in imgFileNames:  # 逐个分析图片的GPS信息
        print('=' * 20 + basename(img_downloaded) + '=' * 20)
        print(FindGPSimage(img_downloaded))


if __name__ == '__main__':
    download_findGPS('http://webtest.qytang.com/gps/gps.html')
