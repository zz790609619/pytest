# 继承
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def study(self):
        print("我是" + self.name + ",我今年" + self.age + "岁,我正在学习")


class Teather(Person):
    def teach(self):
        print("我是" + self.name + ",我今年" + self.age + "岁,我正在教书")

