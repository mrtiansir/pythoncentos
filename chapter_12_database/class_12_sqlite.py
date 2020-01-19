#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import sqlite3
import os

if os.path.exists('test_db.sqlite'):
    os.remove('test_db.sqlite')

teachers_list = [
    {'姓名': '张三', '年龄': 32, '部门': '高一', '学科': '语文'},
    {'姓名': '李四', '年龄': 36, '部门': '高三', '学科': '数学'},
    {'姓名': '王二', '年龄': 42, '部门': '初二', '学科': '美术'}
                 ]

conn = sqlite3.connect('test_db.sqlite')
cursor = conn.cursor()

cursor.execute("create table teachers_info (姓名 varchar(40), 年龄 int, 部门 varchar(40), 学科 varchar(40))")

for teacher in teachers_list:
    name = teacher['姓名']
    age = teacher['年龄']
    department = teacher['部门']
    course = teacher['学科']
    cursor.execute(f"insert into teachers_info values ('{name}', {age}, '{department}', '{course}')")


cursor.execute("select * from teachers_info")
result = cursor.fetchall()

for teacher in result:
    print(teacher)

cursor.execute("select 年龄 from teachers_info where 姓名 = '张三'")
result = cursor.fetchall()
for age in result:
    print(age[0])


cursor.execute("select 姓名 from teachers_info where 年龄 > 35 and 学科 != '语文'")
result = cursor.fetchall()

for name in result:
    print(name[0])


cursor.execute("drop table teachers_info")

conn.commit()




