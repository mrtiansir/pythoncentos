#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from my_python_basic.chapter_13_multi_process import sum_multi
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import random


if __name__ == '__main__':
    freeze_support()  #windows平台这加这句，并且一定要放在if __name__ == '__main__':下，才能避免RuntimeError
    #多线程
    pool = ThreadPool()    #有效控制并发线程数，默认为内核数（推荐）

    results = []
    for i in range(0, 10):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        result = pool.apply_async(sum_multi, args=(x, y, z))
        results.append(result)

    pool.close()
    pool.join()

    for i in results:
        print(i.get())

    