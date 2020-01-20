#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


username = "admin"
password = "Cisc0123"
base_url = 'https://10.1.1.101/api/'
# 通过POST发送到服务器的认证用的JSON数据
name_pwd = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
# 认证API的URL
login_url = base_url + 'aaaLogin.json'


def get_token():
    post_response = requests.post(login_url, json=name_pwd, verify=False)

    # 从响应的JSON数据中提取Token的值
    auth = post_response.json()

    auth_token = auth['imdata'][0]['aaaLogin']['attributes']['token']
    # 返回Token的值
    return auth_token


def get_session():
    # request维持会话
    client = requests.session()
    # 会话登录,获取Cookie中的Token
    client.post(login_url, json=name_pwd, verify=False)
    # 返回会话
    return client


if __name__ == "__main__":
    print(get_token())
