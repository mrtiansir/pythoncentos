#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import requests

client = requests.session()

username = "admin"
password = "Cisc0123"

csr1_ip = "10.1.1.253"
csr2_ip = "10.1.1.252"

headers = {'Accept': 'application/yang-data+json', 'Content-Type': 'application/yang-data+json'}

