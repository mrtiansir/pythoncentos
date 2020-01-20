#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, render_template

node = Flask(__name__)


# 处理复杂数据部分,@node.route('/complexdata', methods=['GET']),需要的类
class MyClass:
    def func(self):
        return 'func'


# 处理复杂数据部分,@node.route('/complexdata', methods=['GET']),需要的函数
def myfunc():
    return 'myfunc'


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


if __name__ == "__main__":
    # 运行Flask在host='10.1.1.100', port=80
    # 在linux上可以使用'0.0.0.0'
    node.run(host='10.1.1.100', port=80)
