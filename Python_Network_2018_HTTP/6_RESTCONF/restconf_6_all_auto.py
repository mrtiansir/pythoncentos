#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from restconf_0_core_info import client, username, password, csr1_ip, csr2_ip, headers
from restconf_1_create_interface import create_interface
from restconf_2_config_if_ip import config_interface_ip
from restconf_3_no_shutdown import no_shutdown_if
from restconf_4_ospf_process_router_id import ospf_process_router_id
from restconf_5_ospf_network import ospf_network

csr1_ifs = [["GigabitEthernet2", ["192.168.1.1", "255.255.255.0"]], ["Loopback0", ["1.1.1.1", "255.255.255.0"]]]
csr2_ifs = [["GigabitEthernet2", ["192.168.1.2", "255.255.255.0"]], ["Loopback0", ["2.2.2.2", "255.255.255.0"]]]

csr1_ospf = {"process_id": 1, "router_id": "1.1.1.1", "area": [[0, [["192.168.1.0", "0.0.0.255"], ["1.1.1.0", "0.0.0.255"]]]]}
csr2_ospf = {"process_id": 1, "router_id": "2.2.2.2", "area": [[0, [["192.168.1.0", "0.0.0.255"], ["2.2.2.0", "0.0.0.255"]]]]}

# 配置CSR1接口IP,并且no shutdown接口
for csr1_if in csr1_ifs:
    if "Loopback" in csr1_if[0]:
        create_interface(csr1_ip, username, password, csr1_if[0])
    config_interface_ip(csr1_ip, username, password, csr1_if[0], csr1_if[1][0], csr1_if[1][1])
    no_shutdown_if(csr1_ip, username, password, csr1_if[0])

# 配置CSR2接口IP,并且no shutdown接口
for csr2_if in csr2_ifs:
    if "Loopback" in csr2_if[0]:
        create_interface(csr2_ip, username, password, csr2_if[0])
    config_interface_ip(csr2_ip, username, password, csr2_if[0], csr2_if[1][0], csr2_if[1][1])
    no_shutdown_if(csr2_ip, username, password, csr2_if[0])

# 配置CSR1 OSPF进程,与Router-ID
ospf_process_router_id(csr1_ip, username, password, csr1_ospf["process_id"], csr1_ospf["router_id"])

# CSR1 宣告网络
for area in csr1_ospf["area"]:
    for network in area[1]:
        ospf_network(csr1_ip, username, password, csr1_ospf["process_id"], network[0], network[1], area[0])

# 配置CSR2 OSPF进程,与Router-ID
ospf_process_router_id(csr2_ip, username, password, csr2_ospf["process_id"], csr2_ospf["router_id"])

# CSR2 宣告网络
for area in csr2_ospf["area"]:
    for network in area[1]:
        ospf_network(csr2_ip, username, password, csr2_ospf["process_id"], network[0], network[1], area[0])
