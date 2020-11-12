import csv  # 系统内置模块

import time
import socket
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


def test(xx, y, q):  # Use thread.start_new_thread() to create 2 new threads
    for count in range(y, q):
        row = xx[count]
        ss = 'E:/wwwww/' + row[2]
        mkdir(ss)
        try:
            request.urlretrieve(row[0] + '?x-oss-process=image/resize,h_200,w_450/quality,Q_60',
                                ss + '/门头像_' + row[3] + '.png')
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    request.urlretrieve(row[0] + '?x-oss-process=image/resize,h_200,w_450/quality,Q_60',
                                        ss + '/门头像_' + row[3] + '.png')
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
            if count > 5:
                print("downloading picture fialed!")
        try:
            if row[1] is not None:
                request.urlretrieve(row[1] + '?x-oss-process=image/resize,h_200,w_450/quality,Q_60',
                                    ss + '/身份证正面照_' + row[3] + '.png')
        except socket.timeout:
            size = 1
            while size <= 5:
                try:
                    request.urlretrieve(row[1] + '?x-oss-process=image/resize,h_200,w_450/quality,Q_60',
                                        ss + '/身份证正面照_' + row[3] + '.png')
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    size += 1
            if size > 5:
                print("downloading picture fialed!")


if __name__ == '__main__':
    multiprocessing.freeze_support()
    p = multiprocessing.Pool(20)
    for i in range(1, 21):
        if i == 1:
            star = 0
        else:
            star = (i - 1) * 20000
        p.apply_async(test, args=(result, star, i * 20000))
    p.close()
    p.join()
    print("所有进程执行完毕")
