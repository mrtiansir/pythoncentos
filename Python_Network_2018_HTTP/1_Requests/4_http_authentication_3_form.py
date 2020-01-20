#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import requests
from bs4 import BeautifulSoup

URL = 'http://www.qytang.com/accounts/login/'

# 会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie，
# 期间使用 urllib3 的 connection pooling 功能。所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，
# 从而带来显著的性能提升。
# http://docs.python-requests.org/zh_CN/latest/user/advanced.html
client = requests.session()

# 使用BS4分析页面
soup = BeautifulSoup(client.get(URL).content, 'lxml')
# print(client.cookies.get_dict())
# 此时还未认证通过,所以并没有sessionid
print(client.cookies.get('sessionid'))

# 找到页面中'csrfmiddlewaretoken'的值
csrftoken = soup.find('input', attrs={"type": "hidden", "name": "csrfmiddlewaretoken"}).get("value")

# 把用户名,密码,'csrfmiddlewaretoken'的值,通过POST的数据传输给登录页面
login_data = dict(username='admin', password='Cisc0123', csrfmiddlewaretoken=csrftoken)
r = client.post(URL, data=login_data)

# 登录成功获取sessionid
print(client.cookies.get('sessionid'))
# 查看状态码
print(r.status_code)
# 查看历史,你会发现收到了302重定向
print(r.history)
# 访问添加学员信息的页面
r = client.get('http://www.qytang.com/addstudent/')

# 由于已经登录成功,获取了sessionid,并且requests.session()维护回话信息
# 添加学员信息页面被成功打开
print(client.cookies.get('sessionid'))
# print(r.text)
