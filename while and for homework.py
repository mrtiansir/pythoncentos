#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
list1 = ['aaa', 111, (4,5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4,5)]

for x in list1:
    for y in list2:
        if x == y:
            print(str(x) + ' in list1 and list2')
            break
    else:
        print(str(x) + ' only in list1')





