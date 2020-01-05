#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

performances = ['Ventriloquism', 'Amazing Acrobatics']
performances.append('Snake Charmer')
print(",".join(i for i in performances))

events = [1,2,3,4,5,6]
dword = events[3]
events.remove(dword)
print(events)

performances = [{'Ventriloquism':'9:00am'},{'Snake Charmer':'12:00pm'}]
performances.append({'Amazing Acrobatics':'2:00pm'})
performances.append({'Enchanted Elephants':'5:00pm'})
print(performances)

performances.pop()
performances.append({'Enchanted Elephants':'6:00pm'})
print(performances)


performances = [{'Ventriloquism': '9:00am'}, {'Snake Charmer': '12:00pm'}, {'Amazing Acrobatics': '2:00pm'}, {'Enchanted Elephants': '5:00pm'}]
performances.remove({'Ventriloquism': '9:00am'})
print(performances)

list_a = ['python', 'bison', 'lion']
list_b = ['python', 'lion', 'bison']
print(list_a == list_b)

dict_a = {'python':'reptile', 'bison':'mammal', 'lion':'mammal'}
dict_b = {'python':'reptile', 'lion':'mammal', 'bison':'mammal'}
print(dict_a == dict_b)


performances = [['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'], ['Amazing Acrobatics', 'Enchanted Elephants'], ['Snake Charmer', 'Amazing Acrobatics']]
print(performances[0][2])


performances = {'weekdays': ['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'],'saturday': ['Amazing Acrobatics', 'Enchanted Elephants'],'sunday': ['Snake Charmer', 'Amazing Acrobatics']}
print(performances['weekdays'][2])












