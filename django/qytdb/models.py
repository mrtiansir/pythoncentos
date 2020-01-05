from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.utils import timezone


class Courses(models.Model):
    courses_name = models.CharField(max_length=100, blank=False, primary_key=True)
    courses_summary = models.CharField(max_length=10000, blank=False)
    courses_teacher = models.CharField(max_length=100, blank=False)
    courses_method = models.CharField(max_length=100, blank=False)
    courses_characteristic = models.CharField(max_length=100, blank=True)
    courses_provide_lab = models.CharField(max_length=100, blank=False)
    courses_detail = models.CharField(max_length=10000, blank=False)


class QytangDB(models.Model):
    # verbose_name只影响后台管理的显示
    # blank 决定客户是否可以不输入
    # null 表示值是否可以为NULL
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='姓名')
    age = models.IntegerField(default=18, verbose_name='年龄')
    status = models.BooleanField(default=True, verbose_name='状态', )
    # 注意校验只对后台管理生效
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="Phone format: '13911153335'. 11 digits allowed.")
    phone = models.CharField(validators=[phone_regex],
                             max_length=11,
                             blank=False,
                             null=True,
                             # unique=True,
                             verbose_name='电话')
    # 注意选项只对后台管理生效
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.IntegerField(choices=gender_choices, default=1, verbose_name='性别')
    insert_time = models.DateTimeField(verbose_name='创建时间')
    # auto_now - updates the value of field to current time and date every time the Model.save() is called.
    # auto_now_add - updates the value with the time and date of creation of record.
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

# class Coursestatus(models.Model):
#     courses_name = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)


class CoursesDB(models.Model):
    courses_name = models.CharField(max_length=100)


# 默认关联到主键，默认的主键为唯一ID
# CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
# PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
# SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
# SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
# SET(): 自定义一个值，该值当然只能是对应的实体了

class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=False)
    courses_id = models.ForeignKey(CoursesDB, on_delete=models.CASCADE)
    age = models.IntegerField()


# 默认关联到主键，默认的主键为唯一ID
class Students(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)
    courses_id = models.ForeignKey(CoursesDB, blank=True, null=True, on_delete=models.SET_NULL)


class StudentsDB(models.Model):
    # 名字,最大长度50,可以为空 (注意:并没有min_length这个控制字段)
    name = models.CharField(max_length=50, blank=False)

    # 电话号码,校验以1开头的11位数字,最大长度为11,不可以为空,唯一键(注意:并没有min_length这个控制字段)
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="Phone number must be entered in the format: '13911153335'. 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=False, unique=True)

    # QQ号,校验5到20位的数字,最大长度为20,不可以为空,唯一键(注意:并没有min_length这个控制字段)
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ number must be entered in the format: '605658506'. 5-20 digits allowed.")
    qq_number = models.CharField(validators=[qq_regex], max_length=20, blank=False, unique=True)

    # 邮件,EmailField会校验邮件格式,最大长度50, 可以为空(注意:并没有min_length这个控制字段)
    mail = models.EmailField(max_length=50, blank=True)

    # 学习方向,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = models.CharField(max_length=5, choices=direction_choices)

    # 班主任,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = models.CharField(max_length=2, choices=class_adviser_choices)

    # 缴费情况,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    payed_choices = (('已缴费', '已缴费'), ('未交费', '未交费'))
    payed = models.CharField(max_length=3, choices=payed_choices)

    # 报名日期,自动添加日期项
    date = models.DateField(auto_now_add=True)
