import csv  # 系统内置模块
import socket
import urllib.request as request
from logging import getLogger, INFO
from concurrent_log_handler import ConcurrentRotatingFileHandler
import os

import multiprocessing

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
    if not os.path.exists(path):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print (path + ' 创建成功')
        return True
    else:
        return False


# 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
#
# urllib.request.urlretrieve('http://cxsq-test.oss-cn-shanghai.aliyuncs.com/merchant/2d8c6da7a8d4406da132a143563c49d4',
#                    'D:/1.jpg')
# csv文件读写 csv每一行用,分割 换行则是切行

with open('q2w.csv') as fileRead:
    f_csv = csv.reader(fileRead)
    result = list(f_csv)


def test(xx, y, q):  # Use thread.start_new_thread() to create 2 new threads
    if q == 350000:
        q = 350823
    print(str(y) + '-' + str(q - 1))
    for count in range(y, q):
        row = xx[count]
        ss = 'D:/zzzzz/' + row[2]
        if mkdir(ss):
            reul = ''
            try:
                request.urlretrieve(row[0],
                                    ss + '/门头像_' + row[3] + '.png')
                reul += ','
            except Exception as e:
                print("m")
                reul += str(row[0]) + ","
                print(e)
            try:
                if row[1] is not None and row[1] != '':
                    request.urlretrieve(row[1],
                                        ss + '/身份证正面照_' + row[3] + '.png')
                reul += ','
            except Exception as e:
                print("f" + str(row[1]))
                reul += str(row[1]) + ','
                print(e)
            if reul[0] is not ',':
                reul += str(row[2])
                log.info(reul)


# 350822

if __name__ == '__main__':
    multiprocessing.freeze_support()
    p = multiprocessing.Pool(10)
    for i in range(1, 11):
        if i == 1:
            star = 0
        else:
            star = (i - 1) * 35000
        p.apply_async(test, args=(result, star, i * 35000))
    p.close()
    p.join()
    print("所有进程执行完毕")
