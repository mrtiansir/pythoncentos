import re

str1 = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match('\s*(\w+)\s+server\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)\s+localserver\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+),\s+idle\s+(\d+:\d+:\d+),\s+bytes\s+(\d+),\s+flags\s+(\w+)',str1).groups()

split_idle = result[3].split(':')

hours = split_idle[0]
mins = split_idle[1]
seconds = split_idle[2]

print(f'{"protocol":<20}: {result[0]}')
print(f'{"server":<20}: {result[1]}')
print(f'{"localserver":<20}: {result[2]}')
print(f'{"idle":<20}: {hours:<2}小时 {mins:<2}分钟 {seconds:<2}秒')
print(f'{"bytes":<20}: {result[4]}')
print(f'{"flags":<20}: {result[5]}')
