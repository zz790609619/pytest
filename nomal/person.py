class User:
    name = ''
    age = 0

    # 类方法
    def prn(self, address):
        print('我的名字：' + self.name + '我今年' + str(self.age) + "岁，我住在" + address)


__user = User()
prns = __user.prn
