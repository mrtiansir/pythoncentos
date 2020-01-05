#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

# str = 'haier'
# for c in str:
#     print(c, end='')


dict = {'test' : 12345.1234}
str = '%(test)-10.2f' % dict
print(str)