# 文件操作
# open(文件路径，读取方式，编码方式)
files = open('../zz.txt', encoding='utf8')
print(files.read())

import csv  # 系统内置模块

# csv文件读写 csv每一行用,分割 换行则是切行
filez = open('../mer.csv', 'w')
z = csv.reader(filez)
print(z)
w = csv.writer(filez)
w.writerow(["18888888", 'zz'])  # 会覆盖

# 写入内存c
from io import StringIO

s_io = StringIO()

print('hello', file=s_io)
print(s_io.getvalue())

# 记日志 未完成
import sys


def log(fn):
    def inner():
        fn()
        sys.stderr = open("../error.txt", 'w', encoding='utf8')  # 捕捉控制台错误
        sys.stdout = open("../out.txt", 'w', encoding='utf8')  # 捕捉控制台正常输入

    return inner


@log
def devidess():
    print("xx")
    print(1 / 0)


devidess()
