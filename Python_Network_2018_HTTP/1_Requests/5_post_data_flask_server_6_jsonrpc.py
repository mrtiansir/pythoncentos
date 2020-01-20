#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, request
import json
import datetime

node = Flask(__name__)


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


if __name__ == "__main__":
    # 运行Flask在host='10.1.1.100', port=80
    # 在linux上可以使用'0.0.0.0'
    node.run(host='10.1.1.100', port=80)
