#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import pickle

dbfile = open('test_db.pl', 'rb')
db = pickle.load(dbfile)
print(db)

for key,value in db.items():
    print(key, '=>', value)


if __name__ == '__main__':
    pass
    