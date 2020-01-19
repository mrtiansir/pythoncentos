#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from chapter_12_database.class_12_initdata import db
from datetime import date
import pickle

dbfile = open('test_db.pl', 'wb')     #打开文件，以二进制方式写入
pickle.dump(db, dbfile)      #将db对应的python对象以字节流方式写入到文件dbfile
dbfile.close()    #关闭文件

dbfile = open('test_db.pl', 'ab')
pickle.dump({'today': date.today()}, dbfile)   #将datetime对象以字节流方式写入到文件dbfile
dbfile.close()


if __name__ == '__main__':
    pass
    