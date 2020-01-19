#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

tom = {'name': 'Tom Smith', 'age': 38, 'pay': 10000, 'job': 'software'}
jim = {'name': 'Jim Green', 'age': 35, 'pay': 10000, 'job': 'hardware'}
tina = {'name': 'Tina Doe', 'age':35, 'pay':15000, 'job': 'manager'}

db = {'tom': tom, 'jim': jim, 'tina': tina}


if __name__ == '__main__':
    for key,value in db.items():
        print(key, '=>', value)

    