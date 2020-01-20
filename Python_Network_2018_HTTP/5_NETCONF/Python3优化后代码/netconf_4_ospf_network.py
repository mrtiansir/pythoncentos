#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import lxml.etree as ET
from ncclient import manager
from ncclient.operations import RPCError


def netconf_ospf_network(ip, username, password, process_id, network, mask, area_id, port='830'):
    # yang-explorer 产生的XML
    # xmlns为前缀,防止命名冲突
    payload_xml = """
            <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
              <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" xmlns:ios-ospf="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <router>
                  <ios-ospf:ospf>
                    <ios-ospf:id>1</ios-ospf:id>
                    <ios-ospf:network>
                      <ios-ospf:ip>192.168.1.0</ios-ospf:ip>
                      <ios-ospf:mask>255.255.255.0</ios-ospf:mask>
                      <ios-ospf:area>0</ios-ospf:area>
                    </ios-ospf:network>
                  </ios-ospf:ospf>
                </router>
              </native>
            </config>
    """
    # 转换字符串到XML
    root = ET.fromstring(payload_xml)
    # 查找id,并把它的文本部分修改为客户输入的OSPF进程ID
    # 由于使用了xmlns前缀,所以在搜索和处理元素的时候,都需要添加前缀
    for id_xml in root.iter("{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf}id"):
        id_xml.text = str(process_id)
    for ip_xml in root.iter("{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf}ip"):
        ip_xml.text = network
    for mask_xml in root.iter("{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf}mask"):
        mask_xml.text = mask
    for area_xml in root.iter("{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf}area"):
        area_xml.text = str(area_id)
    # 打印最终生成的XML
    print(ET.tostring(root).decode())

    # 把最终构建的XML,转换到字符串,并且使用NETCONF客户端ncclient,发送到网络设备
    payload_xml = ET.tostring(root).decode()

    # 使用NETCONF客户端ncclient,连接网络设备
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            # 发送构建的XML数据,到网络设备,修改配置(edit_cofig)
            response = m.edit_config(target='running', config=payload_xml).xml
            # 从字符串数据转换到XML
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # 从XML数据,转换到字符串,并返回
        return ET.tostring(data).decode()


if __name__ == '__main__':
    # print(netconf_ospf_network('10.1.1.253', 'admin', 'Cisc0123', 1, '192.168.1.0', '0.0.0.255', 0))
    print(netconf_ospf_network('10.1.1.253', 'admin', 'Cisc0123', 1, '1.1.1.0', '0.0.0.255', 0))