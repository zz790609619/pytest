# 定义类
# 1. class 类名
# 2. class 类名(Object)
# __new__ 是new一个方法 如果不重写则调用object的__new__方法
class User:
    # 类的字段 放在__init__方法里 如果不想被随意添加 增加__slots__ =（'可被访问的属性'）
    # __slots__ = ('name', 'age')
    type = '人类'  # 类属性
    __count = 0

    def __init__(self, name, age):
        User.__count += 1
        self.name = name
        self.age = age
        # self.__money = 1000  # 以__开头的都是私有变量

    def get_count(self):
        return self.__count

    # 类方法
    def prn(self, address):
        print('我的名字：'+self.name + '我今年' + self.age+"岁，我住在"+address)

    def __call__(self, *args, **kwargs):
        print('xx')

    # 重写equals方法  is 判断内存地址  ==判断的值(__eq__)
    def __eq__(self, other):
        print("xxx")

    # 转换成字典后 user1["age"]=25实际调用了
    def __setitem__(self, key, value):
        self.__dict__["key"] = value

    # 转换成字典后 user1["age"]实际调用了
    def __getitem__(self, key, value):
        self.__dict__["key"] = value


# 1. User('xx', '18')调用了__new__方法，在内存中开辟一个区域给这个
# 2. 调用了__init__方法，将self指向这个内存空间
user1 = User('xx', '18')
user1.prn("苏州")

#    实例对象(user1)      类对象(User)
# 实例对象增加字段只影响自己，不影响类对象，类对象新增字段，如果实例对象没有该字段，则会影响所有没有该字段的实例对象，如果实例对象有，则取自己的
# user1.address = "xxx"


# user1() 实际调用的是__call__方法 本质上用了装饰器模式
# def sss(x, y):
#     print(x + y)
# user2= user1('ss', 'xx', sss(1, 2))


def test(x, y):
    print(x + y)

# 获取私有变量的方式

# 判断当前模块名字，判断是否是当前名字,如果是运行当前的类，则是"__main__",其他文件则是文件
print(__name__)


# 转成一个字典
print(user1.__dict__)
user1["age"] = 20
print(user1.age)
print(user1.get_count())

if __name__ == "__main__":
    test(1, 2)




