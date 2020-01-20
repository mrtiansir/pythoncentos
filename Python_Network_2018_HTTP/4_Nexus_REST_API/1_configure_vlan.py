#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from login import get_token, get_session
import requests
# 参考文档
# https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-x/#!configuring-vlans/creating-a-vlan
vlan_url = "http://10.1.1.101/api/mo/sys/bd.json"


def configure_vlan_cookie(vlanid):
    # 头部需要声明数据为json,并放入Cookie值
    my_headers = {'content-type': 'application/json', 'Cookie': "APIC-Cookie=" + get_token()}
    # 创建VLAN的JSON数据
    payload = {"bdEntity": {
                                "children": [
                                                {"l2BD": {
                                                            "attributes": {
                                                                            "fabEncap": "vlan-"+str(vlanid),
                                                                            # "pcTag": "1"
                                                                          }
                                                          }
                                                }
                                            ]
                            }
                }
    # 发起POST请求
    r = requests.post(vlan_url, headers=my_headers, json=payload, verify=False)
    # 返回回显的JSON数据
    print(r.json())


def configure_vlan_session(vlanid):
    # 获取登录成功的会话
    session = get_session()
    # 头部需要声明数据为json
    my_headers = {'content-type': 'application/json'}
    # 创建VLAN的JSON数据
    payload = {"bdEntity": {
                                "children": [
                                                {"l2BD": {
                                                            "attributes": {
                                                                            "fabEncap": "vlan-"+str(vlanid),
                                                                            # "pcTag": "1"
                                                                          }
                                                          }
                                                }
                                            ]
                            }
                }
    # 发起POST请求
    r = session.post(vlan_url, headers=my_headers, json=payload, verify=False)
    # 返回回显的JSON数据
    print(r.json())


def delete_vlan(vlanid):
    # 获取登录成功的会话
    session = get_session()
    # 头部需要声明数据为json
    my_headers = {'content-type': 'application/json'}
    # 创建VLAN的JSON数据
    payload = {"bdEntity": {
                                "children": [
                                                {"l2BD": {
                                                            "attributes": {
                                                                            "fabEncap": "vlan-"+str(vlanid),
                                                                            "status": "deleted"
                                                                          }
                                                          }
                                                }
                                            ]
                            }
                }
    # 发起POST请求
    r = session.post(vlan_url, headers=my_headers, json=payload, verify=False)
    # 返回回显的JSON数据
    print(r.json())


class Vlan:
    def __init__(self, vlanid, state):
        self.vlanid = vlanid
        self.state = state

    def __repr__(self):
        return "VLANID: %-5s State: %s" % (self.vlanid, self.state)


def show_vlan_all():
    # 获取登录成功的会话
    session = get_session()

    all_vlan_url = "http://10.1.1.101/api/mo/sys/bd.json?rsp-subtree=children"

    r = session.get(all_vlan_url, verify=False)

    # 提取返回的json数据
    result_json = r.json()

    vlan_list = []

    # 提取每一个VLAN的ID和RN信息
    for vlan_json in result_json['imdata'][0]['bdEntity']['children']:
        # print(vlan_json['l2BD']['attributes'])
        vlan_list.append(Vlan(vlan_json['l2BD']['attributes']['id'], vlan_json['l2BD']['attributes']['BdState']))

    return vlan_list


if __name__ == "__main__":
    # configure_vlan_cookie(266)
    configure_vlan_session(966)
    for vlan in show_vlan_all():
        print(vlan)
    delete_vlan(966)
    for vlan in show_vlan_all():
        print(vlan)
