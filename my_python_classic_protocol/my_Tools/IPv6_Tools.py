#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import re

def full_ipv6(ipv6):
    '''输入简略ipv6地址，得出全格式ipv6地址'''
    ipv6_section = ipv6.split(":")   #对原始地址使用":"进行分割

    ipv6_section_len = len(ipv6.split(":"))    #了解原始地址的分段数量

    if ipv6_section.index(''):      #var.index('str')，返回在str在var中的位置
        null_location = ipv6_section.index('')     #找到空位，原始ipv6地址中的::部分，被":"分隔后结果为''
        ipv6_section.pop(null_location)  #把原来的空位弹出去
        add_section = 8 - ipv6_section_len + 1  #计算需要补'0000'的段数，需要被几段'0000'

        for x in range(add_section):
            ipv6_section.insert(null_location, '0000')   #开始补'0000',在ipv6_section列表中需要补'0000'的位置开始插入'0000',插入数量为add_section

        new_ipv6 = []

        for s in ipv6_section:
            if len(s) < 4:
                new_ipv6.append((4 - len(s)) * '0' + s)   #对于长度不够4位的section,左边补0
            else:
                new_ipv6.append(s)
        return ':'.join(new_ipv6)    #使用":"连接在一起成为完整的ipv6地址
    else:
        return ipv6

def solicited_node_multicast_address(ipv6):
    '''输入GLUA ipv6地址，获取对应被请求节点组播地址'''
    return "FF02::1:FF" + full_ipv6(ipv6)[-7:].upper()    #拼接得到被请求节点组播地址（前缀固定，后24bit继承GLUA地址的后24bit）

def mac_to_ipv6_linklocal(mac):
    '''输入mac地址，获取对应的linklocal ipv6地址'''
    # 将以.:-分隔的mac中的分隔符去掉,以小写输出
    eui64 = re.sub(r'[.:-]', '', mac).lower()
    # mac地址中间加入fffe
    eui64 = eui64[0:6] + 'fffe' + eui64[6:]
    # ^是XOR（异或）计算，相同取0，不同取1
    # zfill，返回指定长度的字符串，输出结果右对齐，前面填充0
    # Convert hex to binary(16进制转二进制)：
    # my_hexdata = "1a"
    # scale = 16 ## equals to hexadecimal
    # num_of_bits = 8
    # bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    # hex(int(eui64[0:2], 16) ^ 2)输出结果为0x1111111，取[2:]的内容
    eui64 = hex(int(eui64[0:2], 16) ^ 2)[2:].zfill(2) + eui64[2:]

    linklocal_last_section = ':'.join(re.findall('.{4}', eui64))

    ipv6_linklocal = 'FE80::' + linklocal_last_section.upper()

    return ipv6_linklocal

def ipv6_to_mac(ipv6):
    '''输入eui64格式的link_local ipv6地址，得出对应的mac地址'''
    # 得出全格式ipv6地址
    ipv6_sec = ipv6.split(":")   #对原始地址使用":"进行分割

    if ipv6_sec[0].lower() == 'fe80':   #判断输入ipv6地址为link_local地址
        try:
            ipv6_address = full_ipv6(ipv6)   #将ipv6地址格式转换为全格式形式
            #使用":"进行分离，并且提取后4个部分
            #['0250', '56ff', 'feab', '4d19']
            last_4_sections = ipv6_address.split(":")[-4:]
            #提取第1个部分的前2位，从16进制转换为二进制，
            #使用2(00000010)异或转换第7位
            mac_1 = hex(int(last_4_sections[0][:2], 16) ^ 2)[2:].zfill(2)
            #提取mac后续部分,从16进制转为二进制，
            mac_2 = hex(int(last_4_sections[0][2:], 16))[2:]
            mac_3 = hex(int(last_4_sections[1][:2], 16))[2:]
            mac_4 = hex(int(last_4_sections[2][2:], 16))[2:]
            mac_5 = hex(int(last_4_sections[3][:2], 16))[2:]
            mac_6 = hex(int(last_4_sections[3][2:], 16))[2:]

            mac_addr = str(mac_1) + ":" + str(mac_2) + ":" + str(mac_3) + ":" + str(mac_4) + ":" + str(mac_5) + ":" + str(mac_6)
            return mac_addr

        except Exception:
            pass
    else:
        print('请输入正确的link_local ipv6地址')



if __name__ == '__main__':
    # print(solicited_node_multicast_address('2002::6af7:28ff:fee0:5e9e'))
    # print(mac_to_ipv6_linklocal('68:f7:28:e0:5e:9e'))
    print(ipv6_to_mac('FE80::6AF7:28FF:FEE0:5E9E'))
