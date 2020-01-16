#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts



#使用class来记录netflow的信息
class Netflow:
    def __init__(self, flowid, sip, dip, sport, dport, pro):
        self.flowid = flowid
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.pro = pro

    def __str__(self):
        return f'<{self.__class__.__name__} => {self.flowid}, {self.sip}, {self.dip}, {self.sport}, {self.dport}, {self.pro}>'

if __name__ == '__main__':
    flow1 = Netflow(3789, '10.159.202.100', '202.102.134.68', '1025', '23', 'tcp')
    print(flow1)
    print(flow1.sip)


    