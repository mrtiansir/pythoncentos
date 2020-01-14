#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
'''
python v3.6以后引入的字符串格式用户
f'{var1:formatspec}{var2:formatspec}{var3:formatspec}'
'''

department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

sec = f'Department1 name:{department1:<10s} Manager:{depart1_m:<10s} COURSE_FEES:{COURSE_FEES_SEC:<10.2f}'
python = f'Department2 name:{department2:<10s} Manager:{depart2_m:<10s} COURSE_FEES:{COURSE_FEES_Python:<10.2f}'

print('='*68)
print(sec)
print(python)
print('='*68)
