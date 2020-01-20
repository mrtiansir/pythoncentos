#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from login import get_token, get_session
# 参考文档
# https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-x/#!configuring-static-routes/configuring-an-ipv4-static-route


def configure_static_route(dest_prefix, next_hop, outboundif, vrf="default"):
    route_url = "http://10.1.1.101/api/mo/sys/ipv4/inst.json"
    # 获取登录成功的会话
    session = get_session()
    # 头部需要声明数据为json
    my_headers = {'content-type': 'application/json'}
    # 配置静态路由的JSON数据
    payload = {"ipv4Inst": {
                                "children": [{
                                                "ipv4Dom": {
                                                            "attributes": {
                                                                            "name": "default"
                                                                          },
                                                            "children": [{
                                                                            "ipv4Route": {
                                                                                            "attributes": {
                                                                                                            "prefix": dest_prefix
                                                                                                          },
                                                                                            "children": [{
                                                                                                            "ipv4Nexthop": {
                                                                                                                            "attributes": {
                                                                                                                                            "nhAddr": next_hop,
                                                                                                                                            "nhIf": outboundif,
                                                                                                                                            "nhVrf": vrf,
                                                                                                                                            # "pref": "1",
                                                                                                                                            # "rtname": "StatRt5",
                                                                                                                                            # "tag": "1234"
                                                                                                                                          }
                                                                                                                            }
                                                                                                        }]
                                                                                        }
                                                                        }]
                                                            }
                                            }]
                            }
              }
    # 发起POST请求
    r = session.post(route_url, headers=my_headers, json=payload, verify=False)
    # 返回回显的JSON数据
    print(r.json())


def show_ipv4_route():
    show_route_url = "https://10.1.1.101/api/mo/sys/ipv4/inst/dom-default/routestat.json?rsp-foreign-subtree=ephemeral&batch-id=1&batch-size=10"
    # 获取登录成功的会话
    session = get_session()

    r = session.get(show_route_url, verify=False)
    # 返回回显的JSON数据
    infs = r.json()['imdata'][0]['ipv4RouteStat']['attributes']['intrInfo'].split(',')
    next_hops = r.json()['imdata'][0]['ipv4RouteStat']['attributes']['nhPrefixMask'].split(',')
    route_dests = r.json()['imdata'][0]['ipv4RouteStat']['attributes']['prefixMask'].split(',')
    return zip(route_dests, next_hops, infs)


if __name__ == "__main__":
    # 名字必须为ethxxx! exxx和ethernetxxx都不行
    configure_static_route("31.2.1.0/24", "1.2.6.5", "eth1/4")
    for x in show_ipv4_route():
        print(x)

