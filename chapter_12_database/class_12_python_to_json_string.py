#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import json
from chapter_12_database.class_12_initdata import tom, jim, tina
print(tom)
print(type(tom))

json_string = json.dumps(tom, ensure_ascii=False)    #将python对象转换成json string，可以直接通过http协议发走
print(json_string)
print(type(json_string))

dict_recv = json.loads(json_string)   #将收到的json string直接转换为python对象字典
print(dict_recv)
print(type(dict_recv))

if __name__ == '__main__':
    pass
    