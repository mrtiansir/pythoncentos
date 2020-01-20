#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import json
from dateutil import parser
from datetime import timedelta

test_str_source = "{'姓名': '张三', '年龄': 39, '出生日期': '1979-05-05', '状态': true}"   #格式错误，json字符串使用"",且ture首字母小写
test_str_change = '{"姓名": "张三", "年龄": 39, "出生日期": "1979-05-05", "状态": true}'

test_dict = json.loads(test_str_change)    #将字符串通过json转换为python字典
print(test_dict)
print(type(test_dict))

new_birday_date = parser.parse(test_dict['出生日期']).date()   #将字符串对象转换为date对象
new_birday_date += timedelta(days=365 * 10)                  #date对象加365*10天

test_dict['出生日期'] = new_birday_date.strftime("%Y-%m-%d")   #date对象转换为sting对象，更新到字典键

print(test_dict)

json_file = open('json_homework.json', 'w', encoding='utf-8')   #打开文件
json.dump(test_dict, json_file, ensure_ascii=False)    #将python字典写入json文件
json_file.close()

json_file = open('json_homework.json', 'r', encoding='utf-8')  #打开文件
test_dict = json.load(json_file)    #读取json文件到python字典
json_file.close()
print(test_dict)




if __name__ == '__main__':
    pass
    