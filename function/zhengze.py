# 正则表达式
# 贪婪模式：尽可能多的匹配 *={1,}
# 非贪婪模式：查询最近的一次匹配 *? ={}
import re

# 第一个是正则匹配规则
# 第二个是匹配得字符串
m = re.search(r'\\\\', 'hello\\world')
print(m)
# 可以加正则表达式
# 1.match  从头匹配 查询到就返回  返回 re.Match object  查询不到就返回None
# 2,search     返回 re.Match object;
# 3,finditer  返回得结果是一个可迭代对象 每一个对象都是re.Match object
# 4.findall   把查找到所有字符串得结果放在一个结果里
# 5.fullmatch  完整匹配

# re.match 对象使用 ?P<xxx>给分组启用别名 xxx
m1 = re.search(r'(?P<xxx>w.*)(r.*)d', 'hello\\world')  # re.Match object
print(m1.span())  # (6, 11) 参数n 默认是第n分组的
print(m1.group())  # 参数可以为分组index或分组别名 没有参数等于m1.group(0)获取第0个分组 就是匹配到的数据
print(m1.group(2))  # rl
print(m1.groups())  # ('wo', 'rl')
print(m1.groupdict('xxx'))  # {'xxx': 'wo'}
# m.span()  返回得是元组 匹配到得字符串得位置 (6, 10)
# m1.group() 正则表达式的分组  匹配到的字符 传参  表示第n个分组
# m1.groups() 把所有分组的数据变成一个元组
# m1.groupdict() 获取到分组组成的字典 参数是分组名

# re.compile 参数是正则表达式
r = re.compile('w.*d')
m2 = r.search('hello world')
print(m2)

# 正则修饰符 是对正则表达式进行修复
# def search(pattern, string, flags=0): flag为正则修饰符
# .* 贪婪模式 但是.不能适配换行 需要在加一个参数flag
m3 = re.search(r'w.*d', 'hello  wor\nld')
print(m3)  # None
m4 = re.search(r'w.*d', 'hello  wor\nld', re.S)
print(m4)  # <re.Match object; span=(7, 13), match='wor\nld'>

# 正则表达式规则
# 1.字母表示它本身  \字母 有特殊含义 大小写一般都是相反的
# 例如 \d=[0-9]  匹配到数字
# \s 打印非打印字符 例如空格 \S分空白字符
# \w 表示匹配到非符号的其他一切东西 = [0-9a-zA-Z_]
# 2. 符号等都是特殊含义  如果要用符号 则用\+就等于'+'
# ()表示一个分组
# .表示匹配到除了换行之外的任意字符
# [] 可选项默认一次 多次则需要用+ [x,y] 闭区间 可以字母也可以数字 也可以相结合
# | 表示或者
# {}用来表示大括号前面的限定的字符数 {n,}表达n次以上 {,n}表达n次以下  {n,m} n-m次区间内
# * = {0,}  + ={1,}
# ? 1:规定前面的元素最多只能出现一次 2: 将贪婪转换成非贪婪模式
# ^ 以指定内容开头 $已指定内容结尾
m5 = re.search(r'(l[0,5])(.*2)', 'hell00  worzd2', re.S)  # <re.Match object; span=(3, 14), match='l0  wor\nld2'>
print(m5.group(1))  # 0:l0  worzd2 1:l0 2:  worzd2
print(re.search(r'(l[0,5]+w)(.*2)', 'hell00worzd2', re.S).group(1))  # 1: l00w
# print(re.search(r'(l[0,5]+w)(.*2)', 'hell06worzd2', re.S).group(1))  # 没有匹配的就会报错
print(re.search(r'(l[0-5a-dx]w)(.*2)', 'hellawxorzd2').group(1))  # [0-5a-dx]表示这个中间字符可以是0-5 a-d 或者 x
print(re.search(r'(l{2}a)', 'hellawxorzd2').group(1))  # lla
# 例如匹配身份证
# (^[0-9]\d{,6}) 以0-9数字开头(^[0-9])并且后五位是数字(\d{,5})
# ([1-2][0-28-9]\d{,2}) [1-2] 第一位是1或2 [0-28-9] 第二位是0，1，2，8，9 \d{,2} 后两位为数字即可
# ....
idCard = re.search('(^[0-9]\d{,5})([1-2][0-28-9]\d{,2})()', '320324199508134166')
print(idCard)

# 正则替换
# re.sub('规则','替换后的字符或者是方法','原数据')替换
t = re.sub(r'\d', 'x', 'sada21ed')
print(t)


# 如果是替换的是方法的话 则sub方法在调用repalcez方法是 传递的x则为re.match匹配到的结果当作参数
def repalcez(x):
    y = int(x.group())
    y *= 2
    return str(y)


t1 = re.sub(r'\d', repalcez, 'sada21ed')
print(t1)

# 贪婪模式和非贪婪模式
content = ' src="https://imgoss.douyucdn.cn/11.png" src1="https://imgoss.douyucdn.cn/112.png"'
s1 = re.search(r'https://.*\.png', content)  # 贪婪模式
print(s1)  # <re.Match object; span=(6, 81), match='https://imgoss.douyucdn.cn/11.png" src1="https://>
s2 = re.search(r'https://.*?\.png', content)  # 非贪婪模式
print(s2)  # <re.Match object; span=(6, 39), match='https://imgoss.douyucdn.cn/11.png'>
