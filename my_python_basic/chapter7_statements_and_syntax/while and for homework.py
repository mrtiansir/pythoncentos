#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

print('第1题：')
print('='*80)
word = 'Welcome'

for a in word:
    print(a)
print('='*80)

print('第2题：')
print('='*80)
performances = {'Ventriloquism':'9:00am',
'Snake Charmer': '12:00pm',
'Amazing Acrobatics': '2:00pm',
'Enchanted Elephants':'5:00pm'}
for showName,showTime in performances.items():
    print(showName + ':' + showTime)
print('='*80)

print('第3题：')
print('='*80)
import random
num = random.randint(1,10)
guess = input('Guess a num between 1 and 10: ')
guess = int(guess)

while guess != num:
    guess = int(input('Guess again: '))
print('You win!')

print('第4题：')
print('='*80)
list1 = ['aaa', 111, (4,5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4,5)]

for x in list1:
    for y in list2:
        if x == y:
            print(str(x) + ' in list1 and list2')
            break
    else:
        print(str(x) + ' only in list1')






