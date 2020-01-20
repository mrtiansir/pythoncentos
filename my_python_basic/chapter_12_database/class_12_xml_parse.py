#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from xml.etree.ElementTree import parse

tree = parse('class_12_test.xml')   #打开分析的xml文件

root = tree.getroot()    #找到根位置

hand_employees = {}
for team in tree.iter(tag='团队'):   #找到团队标签（tag）
    employees_list = []
    for team_in in team.iter(tag='成员'):   #找到团队标签下的成员标签
        employees_list.append(team_in.attrib['name'])  #找到每一个成员的名字，添加进入列表
    hand_employees[team.attrib['name'][:-2]] = employees_list   #把XXX团队的‘团队’去掉，key为团队名称，value为成员列表

print(hand_employees)




if __name__ == '__main__':
    pass
    