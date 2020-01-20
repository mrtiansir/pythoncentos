#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
from chapter_12_database.class_12_initdata import tom, jim, tina
import shelve
from datetime import datetime

db = shelve.open('test_db.shelve')
db['tom'] = tom
db['jim'] = jim
db['tina'] = tina
db['datetime'] = datetime.now()
db.close()


if __name__ == '__main__':
    pass
    