#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import json
from chapter_12_database.class_12_initdata import tom, jim, tina

print('把python对象转换为JSON格式，并且写入文件')
json_file = open('json_file.json', 'w', encoding='utf-8')
json.dump(tom, json_file, ensure_ascii=False)
json.dump(jim, json_file, ensure_ascii=False)
json.dump(tina, json_file, ensure_ascii=False)
json_file.close()


if __name__ == '__main__':
    pass
    