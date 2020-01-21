#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import winreg
import platform


def get_ifname_frome_reg(iface_guids):
    if_names = ['(unknown)' for i in range(len(iface_guids))]
    #打开注册表'HKEY_LOCAL_MACHINE'
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    #打开r'SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}'
    reg_key = winreg.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}')
    # print(reg_key)

    for i in range(len(iface_guids)):
        try:
            # iface_guids是函数get_ifname的输出，结果为列表，内容为注册表里所有曾经存在过的网卡的标识码 \
            # eg. ['{2DA2BDC9-7B01-45EC-87EF-E7AA9145EB0B}', '{7F93B0F2-4B1E-4CB2-A198-FEA1F8B6F410}'] \
            # 尝试打开iface_guides[i]\Connection
            reg_subkey = winreg.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            #如果存在Name,将结果写入列表，并覆盖对应位置的'(unknown)'
            if_names[i] = winreg.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    #返回字典，key为注册表中网卡标识，value为网上名称
    if_names_dict = dict(zip(iface_guids, if_names))
    return if_names_dict

def win_from_ifname_getid(ifname):
    if platform.system() == 'Linux':
        return ifname
    elif platform.system() == 'Windows':
        import winreg
        import netifaces
        x = netifaces.interfaces()
        for key,value in get_ifname_frome_reg(x).items():
            if value == ifname:
                return key
    else:
        print('不支持该操作系统，本脚本只能运行在Linux和Windows平台')

if __name__ == '__main__':
    print(win_from_ifname_getid('pc'))

    