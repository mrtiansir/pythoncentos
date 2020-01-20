#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import exifread
import re


def FindGPSimage(filepath):
    GPS = {}
    Date = ''
    f = open(filepath, 'rb')
    tags = exifread.process_file(f)
    for tag, value in tags.items():
        if re.match('GPS GPSLatitudeRef', tag):
            GPS['GPSLatitudeRef'] = str(value)
        elif re.match('GPS GPSLongitudeRef', tag):
            GPS['GPSLongitudeRef'] = str(value)
        elif re.match('GPS GPSAltitudeRef', tag):
            GPS['GPSAltitudeRef'] = int(str(value))
        elif re.match('GPS GPSLatitude', tag):
            try:
                match_result = re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]', str(value)).groups()
                GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])/int(match_result[3])
            except:
                GPS['GPSLatitude'] = str(value)
        elif re.match('GPS GPSLongitude', tag):
            try:
                match_result = re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]', str(value)).groups()
                GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])/int(match_result[3])
            except:
                GPS['GPSLongitude'] = str(value)
        elif re.match('GPS GPSAltitude', tag):
            GPS['GPSAltitude'] = str(value)
        elif re.match('.*Date.*', tag):
            Date = str(value)
    return {'GPS信息': GPS, '时间信息': Date}
    # ttp://www.gpsspg.com/maps.htm


if __name__ == '__main__':
    print(FindGPSimage(r"C:\Users\Administrator\PycharmProjects\Python_Network_2018_HTTP\8_Spider\Photo_Spider\Download_IMG\gps_test_1.jpg"))

# 运行结果
# {'GPS信息': {'GPSLatitudeRef': 'N', 'GPSLatitude': (39, 58, 38.481445), 'GPSLongitudeRef': 'E', 'GPSLongitude': (116, 17, 59.598999), 'GPSAltitudeRef': 1, 'GPSAltitude': '0'}, '时间信息': '2016:05:25 20:43:46'}
