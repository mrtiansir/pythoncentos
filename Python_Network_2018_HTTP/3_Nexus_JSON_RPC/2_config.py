#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from n9k_core_info import client, nxos1_url, my_headers, username, password
from requests.auth import HTTPBasicAuth


def create_json_cmd_dict(cmd_id, cmd):
    # 产生每一个命令的字典
    json_cmd_dict = {
                        "jsonrpc": "2.0",
                        "method": "cli",
                        "params": {
                                      "cmd": cmd,
                                      "version": 1
                                   },
                        "id": cmd_id
                     }
    # 返回产生的字典
    return json_cmd_dict


def json_rpc_config(config_cmd_list):
    # 首先添加ID为1的"configure terminal"
    json_data = [create_json_cmd_dict(1, "configure terminal")]
    # 后续命令从ID = 2开始
    i = 2
    # 逐个提取命令,产生字典,放入json_data这个列表里边
    for cmd in config_cmd_list:
        json_data.append(create_json_cmd_dict(i, cmd))
        i += 1
    # 发送POST请求
    r = client.post(nxos1_url, headers=my_headers, auth=HTTPBasicAuth(username, password), json=json_data, verify=False)
    # 返回回显的JSON数据
    return r.json()


if __name__ == "__main__":
    # 不必添加"configure terminal",脚本会自动添加
    cmds_list = ["interface loopback8", "ip address 8.7.7.7/32"]
    print(json_rpc_config(cmds_list))
