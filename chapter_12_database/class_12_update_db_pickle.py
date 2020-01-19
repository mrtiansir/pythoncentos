#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import pickle

dbfile = open('test_db.pl', 'rb')
db = pickle.load(dbfile)
dbfile.close()
print(db)

db['tina']['pay'] *= 1.6    #提高工资

dbfile = open('test_db.pl', 'wb')
db = pickle.dump(db, dbfile)
dbfile.close()



if __name__ == '__main__':
    pass
    