#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import sqlite3
import os

if not os.path.exists('class12_homework.sqlite'):
    print('数据库文件不存在!')


conn = sqlite3.connect('class12_homework.sqlite')
cursor = conn.cursor()

###debug

# cursor.execute("select * from student_info")
# result = cursor.fetchall()
# for student in result:
#     print(f'学员姓名:{student[0]:<6s} 学员年龄:{student[1]:<3d} 学员作业数:{student[2]:<3d}')

####debug


user_notify = '''
输入 1 : 查询整个数据库
输入 2 : 基于姓名查询
输入 3 : 基于年龄查询
输入 4 : 基于作业数查询
输入 0 : 退出
'''
while True:
    print(user_notify)
    user_input = input('请选择：')
    if user_input == '0':
        break
    elif user_input == '1':
        cursor.execute("select * from student_info")
        result = cursor.fetchall()

        for student in result:
            print(f'学员姓名:{student[0]:<6s} 学员年龄:{student[1]:<3d} 学员作业数:{student[2]:<3d}')
    elif user_input == '2':
        stu_name = input('请输入学员姓名：')
        if not stu_name:
            continue
        cursor.execute(f"select * from student_info where 姓名='{stu_name}'")
        result = cursor.fetchall()
        if not result:
            print('学员信息未找到！')
        for student in result:
            print(f'学员姓名:{student[0]:<6s} 学员年龄:{student[1]:<3d} 学员作业数:{student[2]:<3d}')
    elif user_input == '3':
        stu_age = input('搜索大于输入年龄的学员，请输入学员年龄：')
        if not stu_age:
            continue
        cursor.execute(f"select * from student_info where 年龄 > {stu_age}")
        result = cursor.fetchall()
        if not result:
            print('学员信息未找到！')
        for student in result:
            print(f'学员姓名:{student[0]:<6s} 学员年龄:{student[1]:<3d} 学员作业数:{student[2]:<3d}')
    elif user_input == '4':
        stu_homework = input('搜索大于输入作业数的学员，请输入作业数量：')
        if not stu_homework:
            continue
        cursor.execute(f"select * from student_info where 作业数 > {stu_homework}")
        result = cursor.fetchall()
        if not result:
            print('学员信息未找到！')
        for student in result:
            print(f'学员姓名:{student[0]:<6s} 学员年龄:{student[1]:<3d} 学员作业数:{student[2]:<3d}')
    else:
        print('输入错误！请重试')




    