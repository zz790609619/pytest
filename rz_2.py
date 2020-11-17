# -*- coding: UTF-8 -*-
import threading
from time import ctime
import csv  # 系统内置模块
import socket
import urllib.request as request
from logging import getLogger, INFO
from concurrent_log_handler import ConcurrentRotatingFileHandler
import os

socket.setdefaulttimeout(120)

log = getLogger()
# Use an absolute path to prevent file rotation trouble.
logfile = os.path.abspath("wo.log")
# Rotate log after reaching 512K, keep 5 old copies.
rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 512 * 1024, 5)
log.addHandler(rotateHandler)
log.setLevel(INFO)


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print (path + ' 创建成功')
        return True
    else:
        return False


class myThread(threading.Thread):
    def __init__(self, threadID, name, s, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.s = s
        self.e = e

    def run(self):
        print("Starting " + self.name + ctime())
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        # 线程需要执行的方法
        printImg(self.s, self.e)
        # 释放锁
        threadLock.release()


with open('q2w.csv') as fileRead:
    f_csv = csv.reader(fileRead)
    listz = list(f_csv)

    print(listz[40000])
    print(listz[59999])


# 按照分配的区间，读取列表内容，需要其他功能在这个方法里设置
def printImg(s, e):
    print(str(s) + ',' + str(e))
    for count in range(s, e):
        row = listz[count]
        ss = 'D:/zzzzz/' + row[2]
        if listz[count - 1] != listz[count]:
            log.info(ss)
        mkdir(ss)
        if not os.path.exists(ss):
            print(ss)
        reul = ''
        try:
            if not os.path.exists(ss + '/门头像_' + row[3] + '.png'):
                request.urlretrieve(row[0],
                                    ss + '/门头像_' + row[3] + '.png')
                reul += ','
        except Exception as e:
            print("m")
            reul += str(row[0]) + ","
            print(e)
        try:
            if not os.path.exists(ss + '/身份证正面照_' + row[3] + '.png'):
                if row[1] is not None and row[1] != '':
                    request.urlretrieve(row[1],
                                        ss + '/身份证正面照_' + row[3] + '.png')
                reul += ','
        except Exception as e:
            print("f" + str(row[1]))
            reul += str(row[1]) + ','
            print(e)
        # if reul[0] is not ',':
        #     reul += str(row[2])
        #     log.info(reul)


totalThread = 21  # 需要创建的线程数，可以控制线程的数量
#
threadLock = threading.Lock()  # 锁
threads = []  # 创建线程列表
# 创建新线程和添加线程到列表
# 1-21 20000
# 21-41 20000
# 41-61 20000
for i in range(41, 61):
    thread = 'thread%s' % i
    if i == 1:
        star = 0
    else:
        star = (i - 1) * 1000

    thread = myThread(i, "Thread-%s" % i, star, i * 1000)
    threads.append(thread)  # 添加线程到列表

# 等待所有线程完成
for t in threads:
    t.start()
    t.join()
print("Exiting Main Thread")
