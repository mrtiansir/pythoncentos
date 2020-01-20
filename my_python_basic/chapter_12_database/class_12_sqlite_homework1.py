#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import sqlite3
homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

#连接sqlite数据库
conn = sqlite3.connect('class12_homework.sqlite')
cursor = conn.cursor()


#执行创建表操作
cursor.execute("create table student_info (姓名 varchar(40), 年龄 int, 作业数 int)")

#读取python字典中内容，并逐条写入sqlite数据库
for student in homework_dict:
    name = student['姓名']
    age = student['年龄']
    homework = student['作业数']
    cursor.execute(f"insert into student_info values ('{name}', {age}, {homework})")   #格式化字符串，插入数据库时，字符串内容需要加''，数字不加


cursor.execute("select 姓名 from student_info where 姓名 = '学员1'")
result = cursor.fetchall()

for name in result:
    print(name[0])

# cursor.execute("drop table student_info")   #删除表

conn.commit()


if __name__ == '__main__':
    pass
    