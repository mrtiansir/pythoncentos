#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, render_template
import json
from random import randint

node = Flask(__name__)


# Flask 产生线形图
@node.route('/charts/line', methods=['GET'])
def template_charts_line():
    labels = ['2018-8-1', '2018-8-2', '2018-8-3', '2018-8-4', '2018-8-5', '2018-8-6']
    datas = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
    colors = ['#007bff']
    # 需要使用json.dumps,转换Python对象为JSON字符串
    return render_template('4_show_chart.html', labels=json.dumps(labels), datas=json.dumps(datas),
                           colors=json.dumps(colors))


if __name__ == "__main__":
    # 运行Flask在host='10.1.1.100', port=80
    # 在linux上可以使用'0.0.0.0'
    node.run(host='10.1.1.100', port=80)
