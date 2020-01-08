#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
#多级排序的用法，lambda为表达式，将列表中的每一个元素赋值为x，根据后续定义的条件进行排序
#sorted(list, key=lambda x:(condition1, condition2))
import re


port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

# print(sorted(port_list, key=lambda x: (int(re.match('^eth (\d)/(\d\d\d)/(\d)/(\d+)', x).groups()[2]), int(re.match('^eth (\d)/(\d\d\d)/(\d)/(\d+)', x).groups()[3]))))

print(sorted(port_list, key=lambda x: (int(re.match('^eth (\d)/(\d\d\d)/(\d)/(\d\d)', x).groups()[2]), int(re.match('^eth (\d)/(\d\d\d)/(\d)/(\d\d)', x).groups()[3]))))
