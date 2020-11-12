# json的使用 使用场景:前后端交互
# 序列化 dumps 转换成json格式  dump 会存入文件里
# 反序列化 loads json转实体  load 会读去文件中的json
# pickle 将python的任意对象转二进制
import json
import pickle
from po import User

p1 = User.user1
json1 = json.dumps(p1.__dict__)
json2 = pickle.dumps(p1)
print(json1)
print(json2)
p1 = json.loads(json1)  # 转换成字典
print(p1)
p2 = pickle.loads(json2)
print(p2)
