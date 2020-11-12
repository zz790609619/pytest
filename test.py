print("hello world")
# x = input("xxxx")
# print(x + "zz")
z = float("1.0")
print(z)
######
# int float boolean 都有
# 集合
# list 用[] 或 list()
# set 是一个无序的不重复元素序列  用{} 或者set()
# tuple（元祖）使用() 元素不能修改
########
list0 = ["x2", "x1", "xzz"]   # 列表
print(list0)
list1 = {"x", "z", "zx"}
print(list1)
list2 = ("x", "z", "zx")     # 元祖
print(list2)
y = list(list0)
y.sort()
print(y)
####
# dict 字典 类似java的map  key唯一 value不唯一
dicts = {"key1": "value1", "key2": "value2"}
print(dicts.get("key1"))
####
# eval : 内置函数 会执行内部逻辑后再输出
print("1+1")  # 1+1
print(eval("1+1"))  # 2
####
# 计算符
# + 字符，元祖，李彪拼接
# - 用于集合求差
# * 用于字符串，元祖，列表 重复多次
# in  用于字典用来判断key是否存在 列表元祖等遍历 带下标的遍历 enumerate将列表转换成带下标的
list4 = ["x2", "x1", "xzz"]
for e in enumerate(list4):
    print(e)  # (0, 'x2')(1, 'x1')(2, 'xzz')

