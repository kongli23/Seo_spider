# -*- coding: utf-8 -*-

# 集合的创建
s1 = set()
s11 = {1,2,4,2} #可以使用{}创建，但是不能为空，如果为空则为成为字典
s2 = set('hello word')  #它可入迭代数据,如：字符串，列表，元组，它会自动去重复
print(s2)

s3 = set([1,2,3,4,5,5,2,1,4])   #同样列表中的数据也会去重
print(s3)

# 其它常用操作

import random

# 使用推导式生成10个随机数
s4 = {random.randint(1,100) for x in range(10)}
print(s4)

# 上方的推导式等同于
s5 = set()
for k in range(10):
    num = random.randint(1,100)
    s5.add(num)
print(s5)

# 添加
s5.add('hello')
print(s5)

# 删除
s5.remove('hello')  #必须存在才能删除，否则会报error,删除前可以判断
print(s5)

# 更新
s5.update([4,5,6,9,33]) #添加的时候必须添加可迭代类型数据，字符串，列表，集合，元组，它会自动去重
print(s5)

s5.clear()  #清空集合