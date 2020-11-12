class Person(object):
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def work_with(self):
        print(self.name + "在陪着" + self.dog.name + "工作")
        self.dog.dog_work()


class Dog(object):
    def __init__(self, name):
        self.name = name

    def dog_work(self):
        print(self.name + "正在工作")


class PoliceDog(Dog):
    def __init__(self, name):
        self.name = name

    def dog_work(self):
        print(self.name + "正在工作")


p1 = Person("ww", Dog("zz"))
p1.work_with()
