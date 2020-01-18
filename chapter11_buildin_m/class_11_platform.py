#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import sys

result = sys.platform
if 'linux' in result:
    print('this is linux!')
elif 'win' in result:
    print('this is windows!')
else:
    print('other platform')


if __name__ == '__main__':
    pass
    