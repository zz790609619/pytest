# 单例模式  先掉new 在调用 init
class SingleTon(object):
    __instance = None  # 类属性 __是私有的意思
    # 如果不重写new方法，回调用object的new方法

    @classmethod  # 指类方法
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


s1 = SingleTon()
s2 = SingleTon()

print(s1 is s2)
