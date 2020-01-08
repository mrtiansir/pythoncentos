#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
#列表与字典课后作业

#第1题
'''在列表中添加元素
现在有个马戏团想要创建一个程序来记录自己的表演和工作日程，用列表来实现。

创建一个叫performances的列表，有两个元素：'Ventriloquism'和'Amazing Acrobatics'。
使用append()添加一个叫'Snake Charmer'的元素。
打印performances
'''
print('第1题：')
performances = ['Ventriloquism', 'Amazing Acrobatics']
performances.append('Snake Charmer')
print(",".join(i for i in performances))
print('='*100)

#第2题
'''删除列表中的元素 有个列表叫做events，你不知道要删除的元素的值是什么，
但是你知道这个元素的index是3，那么你可以怎么删除这个元素
'''
print('第2题：')
events = [c*4 for c in 'cisco']
events.remove(events[3])
# print(events)
print('='*100)

#第3题
'''添加字典的item
现在我们有一个字典来保存演出的内容和演出的时间，如下： performances = {'Ventriloquism':'9:00am', 'Snake Charmer': '12:00pm'} 演出的内容是key，演出的时间是value。现在要继续向字典中添加内容。
添加key为'Amazing Acrobatics'，value为'2:00pm'的item到字典中。
添加key为'Enchanted Elephants'，value为'5:00pm'的item到字典中。
打印performances。
'''
print('第3题：')
performances = {'Ventriloquism':'9:00am', 'Snake Charmer':'12:00pm'}
performances['Amazing Acrobatics'] = '2:00pm'
performances['Enchanted Elephants'] = '5:00pm'
print(performances)
print('='*100)

#第4题
'''更新字典的item
我们现在有个字典如下：
performances = {'Ventriloquism':'9:00am',
'Snake Charmer': '12:00pm',
'Amazing Acrobatics': '2:00pm',
'Enchanted Elephants':'5:00pm'}
如何将Enchanted Elephants的value更新为6:00pm？
'''
print('第4题：')
performances = {'Ventriloquism': '9:00am', 'Snake Charmer': '12:00pm', 'Amazing Acrobatics': '2:00pm', 'Enchanted Elephants': '5:00pm'}
performances['Enchanted Elephants'] = '6:00pm'
print(performances)
print('='*100)

#第5题
'''更新字典的item
我们现在有个字典如下：
performances = {'Ventriloquism':'9:00am',
'Snake Charmer': '12:00pm',
'Amazing Acrobatics': '2:00pm',
'Enchanted Elephants':'5:00pm'}
如何删除'Ventriloquism'这一个item？
'''
print('第5题：')
performances = {'Ventriloquism': '9:00am', 'Snake Charmer': '12:00pm', 'Amazing Acrobatics': '2:00pm', 'Enchanted Elephants': '5:00pm'}
performances.pop('Ventriloquism')
print(performances)
print('='*100)

#第6题
'''什么时候两个列表是相同的？
下列代码运行的结果是什么？
list_a = ['python', 'bison', 'lion']
list_b = ['python', 'lion', 'bison']
print(list_a == list_b)
'''
print('第6题：')
list_a = ['python', 'bison', 'lion']
list_b = ['python', 'lion', 'bison']
print(list_a == list_b)
print('='*100)

#第7题
'''什么时候2个字典是相同的？
下列代码运行的结果是什么？
dict_a = {'python':'reptile', 'bison':'mammal', 'lion':'mammal'}
dict_b = {'python':'reptile', 'lion':'mammal', 'bison':'mammal'}
print(dict_a == dict_b)
'''
print('第7题：')
dict_a = {'python':'reptile', 'bison':'mammal', 'lion':'mammal'}
dict_b = {'python':'reptile', 'lion':'mammal', 'bison':'mammal'}
print(dict_a == dict_b)
print('='*100)


#第8题
'''列表的列表 马戏团的表演在weekdays、Saturdays和Sundays的是不一样的，我们可以把不同时间的表演放到不同的列表中，但是我们也可以把这些表演放到一个大的列表中。看下面的代码:
分开列表实现
weekdays = ['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'] saturday = ['Amazing Acrobatics', 'Enchanted Elephants'] sunday = ['Snake Charmer', 'Amazing Acrobatics']

用一个大的列表实现
performances = [['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'], ['Amazing Acrobatics', 'Enchanted Elephants'], ['Snake Charmer', 'Amazing Acrobatics']]
如果我们用了上面的这个大的列表实现，那么当我们想要获取'Ventriloquist Vinnie的时候应该怎么写？
'''
print('第8题：')
weekdays = ['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie']
saturday = ['Amazing Acrobatics', 'Enchanted Elephants']
sunday = ['Snake Charmer', 'Amazing Acrobatics']
weekdays.append(saturday)
weekdays.append(sunday)
print(weekdays[2])
print('='*100)

#第9题
'''将列表放到字典中
在上面的例子中，其实将列表放到字典中是个更好的选择，如下：
performances = {'weekdays': ['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'],
'saturday': ['Amazing Acrobatics', 'Enchanted Elephants'],
'sunday': ['Snake Charmer', 'Amazing Acrobatics']}
如果我们想要获取Ventriloquist Vinnie表演，我们要怎么办？
'''
print('第9题：')
day = ['weekdays', 'saturday', 'sunday']
performances = []
performances_1 = ['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie']
performances_2 = ['Amazing Acrobatics', 'Enchanted Elephants']
performances_3 = ['Snake Charmer', 'Amazing Acrobatics']
performances.append(performances_1)
performances.append(performances_2)
performances.append(performances_3)
# print(performances)
dict_perform = dict(zip(day, performances))
print(dict_perform['weekdays'][2])
print('='*100)



#第10题
print('第10题：')
l1 = [4,5,7,1,3,9,0]
l2 = l1.copy()
l2.sort()
for i in range(len(l1)):
    print(l1[i], l2[i])

print('='*100)


#第11题
print('第11题：')
import os
import re
data = os.popen('ifconfig' + ' ens160').read()
# print(data)
result = re.findall('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', data)
for x in result:
    ip = x.split('.')
    if ip[3] == '0':
        netmask = x
    elif ip[3] == '255':
        network = x
    else:
        ip_add = x

print('第一种格式化输出：')
print('%-10s : %-20s' % ("IP地址", ip_add))
print('%-10s : %-20s' % ("子网掩码", netmask))
print('%-10s : %-20s' % ("网络号", network))
print('*'*50)
print('格式化输出方法：')
print('{0:<10s} : {1:<20s}'.format("IP地址", ip_add))
print('{0:<10s} : {1:<20s}'.format("子网掩码", ip_add))
print('{0:<10s} : {1:<20s}'.format("网络号", ip_add))
print('*'*50)
print('f-string格式化输出：')
print(f'{"IP地址":<10s} : {ip_add:<20s}')
print(f'{"子网掩码":<10s} : {netmask:<20s}')
print(f'{"网络号":<10s} : {network:<20s}')
print('='*100)


#第12题
print('第12题：')
result = re.findall('([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})', data)
print(f'{"MAC地址":<5s}: {result[0]:<20s}')
print('='*100)


#第13题
print('第13题：')
s = '''TCP cnc  101.71.30.49:6810 jiankong  192.168.100.62:46421, idle 0:00:28, bytes 54929844, flags UxIO 
TCP cnc  101.71.30.190:6810 jiankong  192.168.100.66:58441, idle 0:00:25, bytes 10423768, flags UxIO 
TCP cnc  101.71.30.190:6820 NVR  192.168.240.2:53684, idle 0:00:04, bytes 98375209, flags UxIO 
TCP cnc  101.71.30.191:6806 jiankong  192.168.100.61:46593, idle 0:00:07, bytes 31711904, flags UxIO 
TCP cnc  101.71.30.192:6810 jiankong  192.168.100.63:34587, idle 0:00:10, bytes 5370656, flags UxIO 
TCP cnc  101.71.4.135:6808 jiankong  192.168.100.64:42712, idle 0:00:28, bytes 20339360, flags UxIO 
TCP cnc  101.71.4.135:6806 jiankong  192.168.100.65:43674, idle 0:00:08, bytes 99677232, flags UxIO 
TCP cnc  101.71.30.206:6804 jiankong  192.168.100.67:54024, idle 0:00:21, bytes 29017881, flags UxIO 
TCP cnc  101.71.4.146:6808 jiankong  192.168.100.69:44250, idle 0:00:06, bytes 38961359, flags UxIO 
TCP cnc  101.71.4.144:6804 jiankong  192.168.100.68:55509, idle 0:00:28, bytes 99694236, flags UxIO'''

list1 = s.split('\n')
# print(list1)
dict1 = {}
for x in list1:
    result = re.match('^[A-Z]+\s+\w+\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}):([0-9]+)\s+\w+\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}):([0-9]+),\s+idle\s+[0-9]+:[0-9]+:[0-9]+,\s+bytes\s+([0-9]+),\s+flags\s+([a-zA-Z]+)', x).groups()
    # print(result)
    conn_key = result[0], result[1], result[2], result[3]
    conn_value = result[4], result[5]
    dict1[conn_key] = conn_value

for key,value in dict1.items():
    print('%10s : %-20s|%10s : %-10s|%10s : %-20s|%10s : %-10s' % ('src', key[0], 'src_p', key[1], 'dst', key[2], 'dst_p', key[3]))
    print(f'{"bytes":>10s} : {value[0]:<20s}|{"flags":>10s} : {value[1]:<20s}')
    print('=' * 110)













