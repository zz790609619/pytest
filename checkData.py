import csv  # 系统内置模块

import time

import urllib.request as request
import threading
import multiprocessing


def mkdir(path):
    # 引入模块
    import os
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


# 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
#
# urllib.request.urlretrieve('http://cxsq-test.oss-cn-shanghai.aliyuncs.com/merchant/2d8c6da7a8d4406da132a143563c49d4',
#                    'D:/1.jpg')
# csv文件读写 csv每一行用,分割 换行则是切行

with open('q2w.csv') as fileRead:
    f_csv = csv.reader(fileRead)
    result = list(f_csv)
    # print(f_csv[0])
    # code = ''
    # count = 0
    # for row in f_csv:
    #     print(row)
    #     ss = 'D:/wwwww/' + row[2]
    #     mkdir(ss)
    #     if code != row[2]:
    #         request.urlretrieve(row[0], 'D:/wwwww/' + row[2] + '/门头像_' + str(count) + '.jpg')
    #         request.urlretrieve(row[1], 'D:/wwwww/' + row[2] + '/身份证正面照_' + str(count) + '.jpg')
    #         count = 0
    #     else:
    #         request.urlretrieve(row[0], 'D:/wwwww/' + row[2] + '/门头像_' + str(count) + '.jpg')
    #         request.urlretrieve(row[1], 'D:/wwwww/' + row[2] + '/身份证正面照_' + str(count) + '.jpg')
    #         count += 1


def test(xx, y, q):  # Use thread.start_new_thread() to create 2 new threads
    for count in range(y, q):
        row = xx[count]
        print(row)
        ss = 'D:/wwwww/' + row[2]
        mkdir(ss)
        request.urlretrieve(row[0], 'D:/wwwww/' + row[2] + '/门头像_' + row[3] + '.jpg')
        if row[1] != 's':
            request.urlretrieve(row[1], 'D:/wwwww/' + row[2] + '/身份证正面照_' + row[3] + '.jpg')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    p = multiprocessing.Pool(20, maxtasksperchild=100)
    for i in range(1, 101):
        if i == 1:
            star = 0
        else:
            star = (i - 1) * 4000
        p.apply_async(test, args=(result, star, i * 4000))
    p.close()
    p.join()
    print("所有进程执行完毕")
