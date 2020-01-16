#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts


from datetime import datetime, date, timedelta, timezone
from dateutil import parser


print(datetime.now() + timedelta(days=60))
print(datetime.now() - timedelta(minutes=1080))
lab_day = '2019-12-20 0:00:00'
lab_day = parser.parse(lab_day)     #将字符串转换为datetime对象，将字符串传入parser函数进行分析，分析出为datetime对象，还可以分析其他类对象
print(lab_day + timedelta(days=90))
# print(lab_day.year)

gmt_8 = timezone(timedelta(hours=8))
gmt_1 = timezone(timedelta(hours=1))

print(datetime.now().astimezone(gmt_8))
print(datetime.now().astimezone(gmt_1))



if __name__ == '__main__':
    pass
    