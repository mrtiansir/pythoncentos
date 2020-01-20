#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from n9k_core_info import client, nxos1_url, my_headers, username, password
from requests.auth import HTTPBasicAuth


def json_rpc_show(show_cmd):
    # 产生JSON数据
    json_data = [
                    {
                        "jsonrpc": "2.0",
                        "method": "cli",
                        "params": {
                                      "cmd": show_cmd,
                                      "version": 1
                                    },
                        "id": 1
                    }
                ]
    # 发起POST请求
    r = client.post(nxos1_url, headers=my_headers, auth=HTTPBasicAuth(username, password), json=json_data, verify=False)
    # 返回回显的JSON数据
    return r.json()


if __name__ == "__main__":
    # print(json_rpc_show("show version"))
    # print(json_rpc_show("show ip inter brie"))
    for vlan in json_rpc_show("show vlan brief")['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']:
        print(vlan)

