#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts
import os

print('开始创建目录和文件：')
print('='*100)
os.mkdir('test')
os.chdir('test')
file1 = open('file1.txt', 'w')
file1.write('test file\n')
file1.write('this is file1\n')
file1.close()
file2 = open('file2.txt', 'w')
file2.write('test file\n')
file2.write('test python\n')
file2.close()
file3 = open('file3.txt', 'w')
file3.write('test file\n')
file3.write('this is python\n')
file3.close()
os.mkdir('file4')
os.mkdir('file5')

print('开始文件类型判断与字符查找：')
print('='*100)
file_names = os.listdir(os.getcwd())
file_list = []
# print(file_names)

for x in file_names:
    if os.path.isfile(x):
        for i in open(x):
            # print(i)
            if 'python' in i:
                file_list.append(x)
    # elif os.path.isdir(x):
    #     print(f'{x:<10s} : {"is a directory":<40s}')
    #     print('*'*50)
    # else:
    #     print(f'{x:<10s} : {"is a unknown file type":<40s}')
print('文件中包含"python"关键字的文件为：')
for a in file_list:
    print(f'{a:^20s}')

print('='*100)
print('开始清理测试目录与文件')
os.chdir('/root/pythoncentos/test')
os.remove('file1.txt')
os.remove('file2.txt')
os.remove('file3.txt')
os.rmdir('file4')
os.rmdir('file5')
os.chdir('..')
os.rmdir('test')
print('所有文件已删除完毕！')
