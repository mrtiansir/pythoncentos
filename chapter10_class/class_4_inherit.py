#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

from chapter10_class.class_2_method import Person

class Manager(Person):   #继承Person类
    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)   #直接调用父系的方法，显示的传入self参数，虽然我们仍旧重新定义了giveraise这个方法，但我们仅仅将传入的百分比增加了10%，然后用它调用通用的方法。这样编码不但可以降低代码冗余，而且涨薪的方法逻辑只在一个地方出现，更加便于修改

    def getfirstname(self):
        return self.name.split()[0]

if __name__ == '__main__':
    jim = Person('Jim Green', 30, 30000, 'software')
    jerry = Manager('Jerry Horse', 40, 50000, 'manager')
    print(jerry.getfirstname())
    print(jim.getlastname())
    jim.giveraise(0.1)
    jerry.giveraise(0.1)
    print(jim.pay)
    print(jerry.pay)



