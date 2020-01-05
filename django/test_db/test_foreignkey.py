#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# 非Django APP需要
from datetime import datetime, timedelta
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qytdjg.settings')
django.setup()
# 非Django APP需要
from qytdb.models import QytangDB


s = QytangDB(name='张婷',
             # age=36,
             status=True,
             phone='239110531',
             gender=2,
             insert_time=datetime.now() + timedelta(hours=2))

s.save()
#
# s1 = QytangDB(name='秦柯',
#               age=39,
#               status=False,
#               phone='13911053',
#               gender=1,
#               insert_time=datetime.now() + timedelta(hours=1))
#
# s1.save()
#
# s2 = QytangDB(name='教主',
#               age=42,
#               status=False,
#               phone='139110531',
#               insert_time=datetime.now())
#
# s2.save()

# s = QytangDB.objects.get(name='教主')
# s.status = True
# s.phone = None
# s.age = 28
# s.save()


# QytangDB.objects.filter(status=True).update(status=False, age=18)
#
# update_dict = {'age': 30, 'status': True, 'phone': 123}
# QytangDB.objects.filter(status=False).update(**update_dict)

# d = QytangDB.objects.get(name='教主')
# d.delete()

# d = QytangDB.objects.filter(age=30)
# d.delete()

# d = QytangDB.objects.all()
# d.delete()

# qytdb.models.DoesNotExist
# qytdb.models.MultipleObjectsReturned
# try:
#     s = QytangDB.objects.get(status=False, name='教主1')
#     print(s.age)
# except QytangDB.DoesNotExist:
#     print('没找到')
# except QytangDB.MultipleObjectsReturned:
#     print('找到多个')


# s = QytangDB.objects.filter(status=False, name='教主1')
# for x in s:
#     print(x.name, x.age)

from django.db.models import Q
# s = QytangDB.objects.filter(Q(name='教主') | Q(status=True))
# for x in s:
#     print(x.name)

# s = QytangDB.objects.filter(name='教主') | QytangDB.objects.filter(status=True)
# for x in s:
#     print(x.name)

# s = QytangDB.objects.filter((Q(name='秦柯') | Q(status=True)) & Q(age__gte=30))
# for x in s:
#     print(x.name)
#
# s = QytangDB.objects.filter(name__regex='^秦.*')
# for x in s:
#     print(x.name)

# s = QytangDB.objects.filter(insert_time__gte=datetime.now())
# for x in s:
#     print(x.name)


# s = QytangDB.objects.filter(phone__isnull=True)
# for x in s:
#     print(x.name)

# from qytdb.models import CoursesDB, Teacher, Students
#
# sec = CoursesDB(courses_name='安全')
# sec.save()
#
# jiaozhu = Teacher(name='教主',
#                   courses_id=CoursesDB.objects.get(courses_name='安全'),
#                   age=16)
#
# jiaozhu.save()
#
# xueyuan1 = Students(name='学员1',
#                     age=16,
#                     teacher_id=Teacher.objects.get(name='教主1'),
#                     courses_id=CoursesDB.objects.get(courses_name='安全'))
#
# xueyuan1.save()
# #
# sec = CoursesDB.objects.get(courses_name='安全')
# sec.delete()

if __name__ == '__main__':
    pass