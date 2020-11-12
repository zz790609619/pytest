###
# 函数
# def 函数名(参数1:类型,参数2:类型)：
# “”“
# 函数说明
# “”“
# return 返回值
# 多返回值时候 列表 元祖 字典
import time
######
# 装饰器模式
# @cal_time 所标记的函数add(i,j)，其实已经变成了 inner(i,j)  而此时的add(i,j)则又被作为fn(i,j) 被执行
#

# -执行逻辑
# 1. 在程序启动的时候 装饰器@cal_time的cal_time函数会先执行，此时的fn是add函数，且inner等于被@cal_time装饰的add函数
# 2. add(a, b)执行的时候，将add函数作为参数fn传入cal_time函数
# 3. 而此时的cal_time是inner函数，会执行inner函数的逻辑
# 3. 在执行inner函数中的参数fn是 才会去真正执行add函数逻辑


def cal_time(fn):
    print("1")
    # def inner(i, *args, **kwargs): 形参

    def inner(i, j, *args, **kwargs):
        time1 = time.time()
        result = 0
        if len(str(args[0])) > 2:
            result = fn(i, j)
        time2 = time.time()
        print(time1 - time2)
        return result

    print("inner ={}".format(inner))
    return inner


@cal_time
def add(i, j):
    """
    注释
    :param i:
    :param j:
    :return:
    """
    return i + j


a = int(input("输入第一个数:"))
b = int(input("输入第二个数:"))
print(add(a, b, "x"))

