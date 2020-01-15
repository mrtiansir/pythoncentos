#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from functools import wraps

def wirte_to_file(filename):
    def decorator(func):
        @wraps(func)   #保持func.__name__ func.__doc__
        def with_write_to_file(*args, **kwargs):
            #以下是装饰器添加的功能
            get_result = func(*args, **kwargs)
            wf = open(filename, 'w')
            wf.write(get_result)
            wf.close()
            #以上是装饰器添加的功能
            return func(*args, **kwargs)   #返回函数

        return with_write_to_file   #返回函数 + 写入返回内容到文件

    return decorator  #返回函数 + 写入返回内容到文件 + 保持func.__name__ func.__doc


if __name__ == '__main__':
    pass
    