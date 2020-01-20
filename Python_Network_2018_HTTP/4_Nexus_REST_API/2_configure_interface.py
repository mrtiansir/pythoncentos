#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from login import get_token, get_session
# 参考文档
# https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-x/#!configuring-vlans/setting-the-access-mode-of-an-interface-to-a-vlan"


def configure_interface_access_vlan(ifname, vlanid):
    interface_url = "http://10.1.1.101/api/mo/sys.json"
    # 获取登录成功的会话
    session = get_session()
    # 头部需要声明数据为json
    my_headers = {'content-type': 'application/json'}
    # 配置接口VLAN的JSON数据
    payload = {
                "topSystem": {
                                "children": [{
                                                "interfaceEntity": {
                                                                    "children": [{
                                                                                    "l1PhysIf": {
                                                                                                    "attributes": {
                                                                                                                    "accessVlan": "vlan-" + str(vlanid),
                                                                                                                    "id": ifname

                                                                                                                  }
                                                                                                }
                                                                                }]
                                                                    }
                                            }]
                             }
              }
    # 发起POST请求
    r = session.post(interface_url, headers=my_headers, json=payload, verify=False)
    # 返回回显的JSON数据
    print(r.json())


def show_interface(name):
    show_interface_url = "http://10.1.1.101/api/mo/sys/intf/phys-[" + name + "].json"
    # 获取登录成功的会话
    session = get_session()

    r = session.get(show_interface_url, verify=False)
    # 返回回显的JSON数据

    result_json = r.json()
    return result_json['imdata'][0]['l1PhysIf']['attributes']


def show_interfaces():
    show_interface_url = "http://10.1.1.101/api/mo/sys/intf.json?rsp-subtree=children"
    # 获取登录成功的会话
    session = get_session()

    r = session.get(show_interface_url, verify=False)
    # 返回回显的JSON数据

    result_json = r.json()
    return result_json['imdata'][0]['interfaceEntity']['children']


if __name__ == "__main__":
    # 名字必须为ethxxx! exxx和ethernetxxx都不行
    configure_interface_access_vlan("eth1/2", 66)
    print(show_interface("eth1/2"))
    for x in show_interfaces():
        print(x)
