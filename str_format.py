#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
'''
字符串格式化方法语法
{fieldname1:formatspec}{fieldname2:formatspec}.format(var1, var2, var3)
'''
department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

sec = 'Department1 name:{0:<10s} Manager:{1:<10s} COURSE_FEES:{2:<10.2f}'.format(department1, depart1_m, COURSE_FEES_SEC)
python = 'Department2 name:{0:<10s} Manager:{1:<10s} COURSE_FEES:{2:<10.2f}'.format(department2, depart2_m, COURSE_FEES_Python)

print('='*68)
print(sec)
print(python)
print('='*68)


