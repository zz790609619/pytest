# 异常处理

# 判断是空 if not xxxx
def dicids(i, j):
    s = 0
    try:
        s = i / j

    except Exception as e:
        print()
    else:
        return s
    finally:
        return s
# 自定义异常 raise 抛出异常


class MyError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(self.x + self.y)


# with 语句 上下文管理器 比如会自动关闭文件/socket/数据库连接
# 后面的 需要有__enter__ 和 __exit__
try:
    with open('../zz.txt') as file:
        print(file.readline())
except Exception as e:
    raise MyError(e)
    print('sad')
finally:
    print('xx')


