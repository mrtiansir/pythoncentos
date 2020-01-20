#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, request, render_template
import json
import datetime
from random import randint

# 后续导入与文件上传有关
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


node = Flask(__name__)
# 配置节点参数
node.config['SECRET_KEY'] = 'welcome to qytang'  # 配置秘钥,用来产生随机数
node.config['UPLOADED_PHOTOS_DEST'] = './upload'  # 定义上传目录,上传的文件最终会保存到这个目录
node.config['WTF_CSRF_ENABLED'] = False  # 关闭CSRF保护

# 实例化UploadSet对象
photos = UploadSet('photos', IMAGES)
# 将app的config配置注册到UploadSet实例photos
configure_uploads(node, photos)


# 处理复杂数据部分,@node.route('/complexdata', methods=['GET']),需要的类
class MyClass:
    def func(self):
        return 'func'


# 处理复杂数据部分,@node.route('/complexdata', methods=['GET']),需要的函数
def myfunc():
    return 'myfunc'


# 上传图片文件的form,继承Flask内建的FlaskForm类
# 一共两个部分:一个部分是文件选择,一个部分是上传按钮
class UploadForm(FlaskForm):
    # 文件选择,配置校验只能为图片文件
    photo_file_1 = FileField(validators=[FileAllowed(photos, u'只能上传图片！'), FileRequired(u'文件未选择！')])
    # 上传按钮
    submit = SubmitField(u'上传')


# 静态路由,最简单页面
@node.route('/template', methods=['GET'])
def template():
    return render_template('1_template_static.html')


# 动态路由,与最简单的模板
@node.route('/template/<name>', methods=['GET'])
def template_name(name):
    return render_template('2_template_dy_user.html', username=name)


# 模板复杂数据的处理
@node.route('/complexdata', methods=['GET'])
def complexdata():
    mydict = {'type': 'dict'}
    mylist = ['list']
    myclass = MyClass()
    return render_template('3_template_complexdata.html',
                           mydict=mydict,
                           mylist=mylist,
                           myclass=myclass,
                           myfunc=myfunc)


# Flask 产生线形图
@node.route('/charts/line', methods=['GET'])
def template_charts_line():
    labels = ['2018-8-1', '2018-8-2', '2018-8-3', '2018-8-4', '2018-8-5', '2018-8-6']
    datas = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
    colors = ['#007bff']
    # 需要使用json.dumps,转换Python对象为JSON字符串
    return render_template('4_show_chart.html', labels=json.dumps(labels), datas=json.dumps(datas),
                           colors=json.dumps(colors))


# Flask接收GET传递的参数与POST传输的数据
@node.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        # 获取GET请求中的参数
        params = request.args.to_dict()
        print(params)
        return "GET参数已经接收"
    elif request.method == 'POST':
        # 获取POST请求中的参数
        data = request.form.to_dict()
        print(data)
        return "POST数据已经接收"


# Flask实现RPC,接收POST JSON数据,处理并返回JSON数据
@node.route('/json', methods=['POST'])
def json_data():
    if request.method == 'POST':
        # 获取POST请求中的JSON数据
        dict = request.get_json()
        print(dict)
        if dict['function'] == 'datetime':  # 如果function为datetime,就返回日期与时间
            return json.dumps({'datetime': str(datetime.datetime.now())})
        elif dict['function'] == 'date':  # 如果function为date,仅返回日期
            return json.dumps({'date': str(datetime.date.today())})


# 文件上传的路径为'/upload',首次访问肯定为'GET',后续提交文件肯定为'POST'
@node.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    # 如果表单提交校验成功
    if form.validate_on_submit():
        filename = photos.save(form.photo_file_1.data)  # 保存上传图片到上传目录,并返回文件名
        file_url = photos.url(filename)  # 通过文件名,产生文件访问的url(用于展示上传成功的图片)
    # 如果校验失败,文件访问的url就为空
    else:
        file_url = None
    # 回显上传文件页面upload.html,传入表单form,如果上传成功就传入文件访问的url(用于展示上传成功的图片)
    return render_template('upload.html', form=form, file_url=file_url)


if __name__ == "__main__":
    # 运行Flask在host='10.1.1.100', port=80
    # 在linux上可以使用'0.0.0.0'
    node.run(host='10.1.1.100', port=80)
