#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from restconf_0_core_info import client, username, password, csr1_ip, csr2_ip, headers
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def ospf_network(ip, username, password, process_id, network, mask, area_id):
    url = "https://" + ip + "/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:ospf/"

    json_data = {
        "ospf": {
            "id": str(process_id),
            "network": {
                "ip": network,
                "mask": mask,
                "area": str(area_id)
            }
        }
    }
    r = client.patch(url, headers=headers, auth=HTTPBasicAuth(username, password), json=json_data, verify=False)
    # 返回回显的JSON数据
    if r.ok:
        print('提交成功')
    else:
        print(r.json())


if __name__ == "__main__":
    ospf_network(csr1_ip, username, password, 1, '1.1.1.0', '0.0.0.255', 0)
