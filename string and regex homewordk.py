#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
#字符串与正则表达式作业
#作业链接：https://gitee.com/qytanggit/Python_Basic/blob/master/Charpter4_Python%E5%86%85%E7%BD%AE%E7%B1%BB%E5%9E%8B_%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%8E%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A.md
#第1题
'''
字符串拼接
通过字符串拼接的方式，打印出QYTANG'day 2014-9-28。不要忘记中间的空格。
'''
print('第1题：')
print('QYTANG' + ' ' + '2014-9-28')
print('='*100)

#第2题
'''
通过切片创建子字符串
现在有个字符串word = " scallywag"，创建一个变量sub_word，通过切片的方式获得字符串"ally"，将字符串的内容赋予sub_word
'''
print('第2题：')
word = 'scallywag'
sub_word = word[2:6]
print(sub_word)
print('='*100)

#第3题
'''
创造自己的语言 我们将在英语的基础上创建自己的语言：在单词的最后加上-，然后将单词的第一个字母拿出来放到单词的最后，然后在单词的最后加上y，例如，Python，就变成了ython-Py。
试着用切片的方式完成这个小游戏。
'''
print('第3题：')
my_word = 'cisco'
my_word_1 = my_word + '-'
my_word_2 = my_word_1[1:] + my_word_1[0]
print('Your new Word is : ' + my_word_2)
print('='*100)

#第4题
print('第4题：')
department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456
print('='*80)
print('Department1 name:%-12s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department1, depart1_m, COURSE_FEES_SEC))
print(f'Department2 name:{department2:<12s} Manager:{depart2_m:<10s} COURSE FEES:{COURSE_FEES_Python:<10.2f} The End!')
print('='*80)

#第5题
print('第5题：')
s = '''Vlan150              10.159.195.2    protocol-up/link-up/admin-up       
Vlan500              10.159.160.124  protocol-up/link-up/admin-up       
Vlan505              10.159.190.124  protocol-up/link-up/admin-up       
Vlan800              10.159.200.2    protocol-up/link-up/admin-up       
Lo0                  10.159.199.1    protocol-up/link-up/admin-up       
Po11.11                 10.159.192.6    protocol-up/link-up/admin-up       
Po12.1899                 10.159.192.14   protocol-up/link-up/admin-up '''

import re

list1 = s.split('\n')
# print(list1)
dict1 = {}
for x in list1:
    result = re.match('(^[a-zA-Z]+[0-9]+\.?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?)\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+([a-z]+-[a-z]+/[a-z]+-[a-z]+/[a-z]+-[a-z]+)', x).groups()
    # print(result)
    dict_key = result[0]
    dict_value = result[1], result[2]
    dict1[dict_key] = dict_value

for key,value in dict1.items():
    print('='*50)
    print(f'{"接口":>10s} : {key:<20s}')
    print(f'{"IP地址":>10s} : {value[0]:<20s}')
    print(f'{"接口状态":>10s} : {value[1]:<20s}')

