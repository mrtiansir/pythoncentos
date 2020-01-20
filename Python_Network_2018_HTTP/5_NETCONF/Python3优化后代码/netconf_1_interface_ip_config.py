#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import lxml.etree as ET
import re
from ncclient import manager
from ncclient.operations import RPCError


def netconf_interface_ip(ip, username, password, interface, address, mask, port='830'):
    # yang-explorer 产生的XML
    # xmlns为前缀,防止命名冲突
    payload_xml = """
    <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>2</name>
            <ip>
              <address>
                <primary>
                  <address>10.1.1.2</address>
                  <mask>255.255.255.0</mask>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
    """
    # 找到客户输入的接口类型和接口ID
    interface_name, interface_no = re.match('([a-zA-Z]*)([0-9].*)', interface).groups()
    # 由于使用了xmlns前缀,所以在搜索和处理元素的时候,都需要添加前缀
    interface_tag = '{http://cisco.com/ns/yang/Cisco-IOS-XE-native}' + interface_name

    root = ET.fromstring(payload_xml)
    for x in root.iter('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}GigabitEthernet'):
        # 设置接口类型, 注意是修改tag,而不是text
        x.tag = interface_tag
    # 查找name,并把它的文本部分修改为客户输入的接口ID
    for name in root.iter("{http://cisco.com/ns/yang/Cisco-IOS-XE-native}name"):
        name.text = interface_no

    # 在Primary下搜索子项目,因为XML里边有两个address tag,所以必须要在Primary下搜索子项目
    for x in root.iter('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}primary'):
        for addr_xml in x.iter('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}address'):
            addr_xml.text = address
    # 查找mask, 并把它的文本部分修改为客户输入的掩码,由于mask tag是唯一的,所以没有必要在Primary下搜索子项目
    for mask_xml in root.iter("{http://cisco.com/ns/yang/Cisco-IOS-XE-native}mask"):
        mask_xml.text = mask

    # 打印整个最终构建的XML
    # print(ET.tostring(root).decode())

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
    # print(netconf_interface_ip('10.1.1.253', 'admin', 'Cisc0123', 'Loopback0', '1.1.1.1', '255.255.255.0', port='830'))
    print(netconf_interface_ip('10.1.1.253', 'admin', 'Cisc0123', 'GigabitEthernet2', '192.168.1.1', '255.255.255.0', port='830'))
