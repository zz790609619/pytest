from collections.abc import Iterable


class nexts(object):
    def __next__(self):
        print('2')
        return 2


class Demo(object):
    def __init__(self, x):
        self.x = x

    # 重写 可让这个类变成 可迭代对象
    def __iter__(self):
        nnexts = nexts()
        return nnexts

    # 下一次
    def __next__(self):
        print('1')
        # return 的东西必须得有
        return self


d = Demo(10)
# isinstance 用来判断一个实例对象是否有指定的类创建出来的
print(isinstance(d, Iterable))

#  循环
for x in d:
    print(x)
