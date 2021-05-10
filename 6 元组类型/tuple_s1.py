# -*- coding: utf-8 -*-

# 元组的创建
t1 = tuple()
print(t1)

# 创建之后就不可以修改
t2 = tuple('hello') #它会将里面的单词完全分割成字母
print(t2)

t3 = tuple([1,2,3,4,5,6])   #它会将列表变成元组
print(t3)

# 元组的遍历
t4 = tuple(range(10))
for i in t4:
    print(i)

# 它同样支持切片，按下标取值

