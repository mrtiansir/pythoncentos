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


def netconf_interface_no_shutdown(ip, username, password, interface, status="true", port='830'):
    # yang-explorer 产生的XML
    # xmlns为前缀,防止命名冲突
    payload_xml = """
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
              <name>GigabitEthernet2</name>
              <enabled>true</enabled>
            </interface>
          </interfaces>
        </config>
    """
    # 转换字符串到XML
    root = ET.fromstring(payload_xml)
    # 查找name,并把它的文本部分修改为客户输入的接口名字
    # 由于使用了xmlns前缀,所以在搜索和处理元素的时候,都需要添加前缀
    for name in root.iter("{urn:ietf:params:xml:ns:yang:ietf-interfaces}name"):
        name.text = interface
    # 查找enabled,并把它的文本部分修改为客户输入的接口状态,默认为true,打开接口!false为关闭接口
    for enable in root.iter("{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled"):
        enable.text = status

    # 打印最终生成的XML
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
    print(netconf_interface_no_shutdown('10.1.1.253', 'admin', 'Cisc0123', 'GigabitEthernet2', status='true'))
