#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import xmltodict
from xml.dom import minidom
import pprint

xml_file = open('class_12_test.xml', 'r').read()  #打开分析的XML文件
xmldict = xmltodict.parse(xml_file, encoding='utf-8')  #读取xml并转换到OrderDict字典[有序字典]
# print(xmldict)
pprint.pprint(xmldict)






#推荐直接对OrderDict字典进行处理
tech_employees = xmldict['root']['公司']['部门'][0]['团队']['成员']    #提取技术部员工
for tech_employee in tech_employees:
    print(tech_employee['@name'])

departs = xmldict['root']['公司']['部门'][0:]     #提取公司部门
for depart in departs:
    print(depart['@name'])


if __name__ == '__main__':
    pass
    