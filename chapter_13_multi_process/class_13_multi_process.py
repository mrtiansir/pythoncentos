#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

from chapter_13_multi_process.class_13_sum_job import sum_multi
from multiprocessing import cpu_count, Pool as ProcessPool     #引入多进程模块中的Pool，在本脚本中别名为ProcessPool
from multiprocessing.pool import ThreadPool     #引入多进程模块中的线程pool
from multiprocessing import freeze_support
import random

if __name__ == '__main__':
    #多进程
    freeze_support()      #Windows平台运行此脚本需要加上这句，并且一定要放在if __name__ == '__main__'下，才能避免RuntimeError
    pool = ProcessPool()   #有效控制并发进程数，默认为内核数（推荐）
    cpus = cpu_count()    #得到内核数的方法
    print(cpus)
    #多线程
    # pool = ThreadPool()
    results = []
    for i in range(0, 10):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        result = pool.apply_async(sum_multi, args=(x, y, z))
        results.append(result)
    #pool.apply_async采用异步方式调用task， pool.apply则是同步方式调用，同步方式意味着下一个task需要等待上一个task完成\
    #后才能开始运行，这显然不是我们想要的功能，所以采用异步方式连接地提交task

    pool.close()
    pool.join() #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool，join函数等待所有子进程结束

    for i in results:
        print(i.get())

    