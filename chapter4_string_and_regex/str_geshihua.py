#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

'''
字符串格式
'%formatpsec1%formatspec2' % (var1, var2)
'''
department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

sec = 'Deparment1 name:%-10s Manager:%-10s COURSE_FEES:%-10.2f' % (department1, depart1_m, COURSE_FEES_SEC)
python = 'Deparment2 name:%-10s Manager:%-10s COURSE_FEES:%-10.2f' % (department2, depart2_m, COURSE_FEES_Python)

print('='*67)
print(sec)
print(python)
print('='*67)

