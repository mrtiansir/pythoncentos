#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

from datetime import datetime, date, timedelta, timezone

five_days_ago = datetime.now() - timedelta(days=5)
now_t = datetime.now()

now_t_str = now_t.strftime('%Y-%m-%d-%H-%M-%S')
file_name = 'save_time_to_file_' + now_t_str + '.txt'

myfile = open(file_name, 'w')
myfile.write(str(five_days_ago))
myfile.close()

gmt_1 = timezone(timedelta(hours=1))
print(datetime.now().astimezone(gmt_1))



if __name__ == '__main__':
    pass
    