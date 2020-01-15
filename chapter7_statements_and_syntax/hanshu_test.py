#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
x = 'old'
def changer():
    global x; x = 'new'
    print(x)


changer()


def squares(x):
    for i in range(x):
        result = yield i ** 2
        print(result)

squares(10)


funcs = [lambda x: x**2, lambda x: x**3]
print(funcs[0](2))


def times(x,y):
    return x*y

print(times(2,3))
print(times([1,2,3,4,5,6],3))


s1 = 'SPAM'
s2 = 'SCAM'

def compare(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

def compare1(seq1,seq2):
    res1 = [x for x in seq1 if x in seq2]
    return res1

print(compare(s1,s2))
print(compare1(s1,s2))


A = 1
def sum(B, C):
    Z = A + B + C
    return Z

print(sum(2,3))

X = 88
def globalfunc():
    global X
    X = 99
    return X

print(globalfunc())

y,z = 1,2
def all_global():
    global x
    x = y + z
    return x

print(all_global())


def f(a):
    a = 77
    return a

print(f(88))


def changer(a,b):
    a = 2
    b[0] = 'cisco'
    return a,b

print(changer(1, [1,2]))

def f(a,b=2,c=3):
    print(a,b,c)
f(1)
f(1,4)
f(1,c=3)


def f(**args):
    print(args)

f(a=1,b=2,c='cisco',p='python')

def f(a,b,c,d):
    print(a+b+c+d)

l = [1,2,3,4]
dict = {'a':1,'b':2,'c':3,'d':5}
f(*l)
f(**dict)


def f(a,*args1,**args2):
    print(a,args1,args2)

f(1,2,3,4,5,6,7,9,10,1,2,34,c='cisco',p='python',h='huawei')


