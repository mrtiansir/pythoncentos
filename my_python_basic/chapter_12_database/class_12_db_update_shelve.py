#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import shelve
from datetime import timedelta

db = shelve.open('test_db.shelve')
tina = db['tina']   #读取数据库键'tina'中的字典
tina['pay'] *= 1.6    #更新字典
db['tina'] = tina   #把更新后的字典重新写回数据库
db.close()

db = shelve.open('test_db.shelve')
datetime_now = db['datetime']
datetime_now += timedelta(days=4)  #在原来的基础上加4天
db['datetime'] = datetime_now   #把更新后的字典重新写回数据库键
db.close()

db = shelve.open('test_db.shelve')
for key,value in db.items():
    print(key, value)
db.close()




if __name__ == '__main__':
    pass
    