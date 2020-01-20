#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, request

node = Flask(__name__)


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


if __name__ == "__main__":
    # 运行Flask在host='10.1.1.100', port=80
    # 在linux上可以使用'0.0.0.0'
    node.run(host='10.1.1.100', port=80)
