#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import shelve
db = shelve.open('test_db.shelve')
for key,value in db.items():
    print(key, '=>', value)
db.close()


if __name__ == '__main__':
    pass
    