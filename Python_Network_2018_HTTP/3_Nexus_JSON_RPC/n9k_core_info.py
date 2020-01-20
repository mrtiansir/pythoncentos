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

client = requests.session()

username = "admin"
password = "Cisc0123"

nxos1_ip = "10.1.1.101"
nxos2_ip = "10.1.1.102"
nxos3_ip = "10.1.1.103"

nxos1_url = "https://" + nxos1_ip + "/ins"
nxos2_url = "https://" + nxos2_ip + "/ins"
nxos3_url = "https://" + nxos3_ip + "/ins"

my_headers = {'content-type': 'application/json-rpc'}

