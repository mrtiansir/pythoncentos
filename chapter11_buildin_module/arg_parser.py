#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

def arg_parser(host, filename, interface):
    print(host)
    print(filename)
    print(interface)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'usage: python arg_parser.py ipaddress -f filename -i interface'

    parser = ArgumentParser(usage=usage)

    parser.add_argument('-f', '--file', dest='filename', help='Write content to FILE', default='1.txt', type=str)   #选项参数
    parser.add_argument('-i', '--interface', dest='interface', help='Specify an interface', default='eth0', type=str)   #选项参数
    parser.add_argument('-t', '--host', dest='host', help='Specify an host', default='10.1.1.1', type=str)    #选项参数
    # parser.add_argument(nargs='?', dest='host', help='Specify an host', default='10.1.1.1', type=str)   #位置参数：'?'表示参数1个可有可无
    # parser.add_argument(nargs='*', dest='hosts', help='Specify some hosts', default='10.1.1.1 10.1.1.2', type=str)  #位置参数，'*'表示参数为多个

    args = parser.parse_args()    #分析传入的参数并赋值给相应的对象

    arg_parser(args.host, args.filename, args.interface)
    # arg_parser(args.hosts, args.filename, args.interface)

    