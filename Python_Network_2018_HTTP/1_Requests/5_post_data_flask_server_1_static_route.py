#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, render_template

node = Flask(__name__)


# 静态路由,最简单页面
@node.route('/template', methods=['GET'])
def template():
    return render_template('1_template_static.html')  # 模板文件在templates目录


if __name__ == "__main__":
    # 运行Flask在host='10.1.1.100', port=80
    # 在linux上可以使用'0.0.0.0'
    node.run(host='10.1.1.100', port=80)
