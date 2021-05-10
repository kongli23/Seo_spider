# -*- coding: utf-8 -*-
# 列表的创建

l = list()
l1 = []
l2 = ''.split()
print(l,l1,l2)

# 带值的列表创建
l3 = list('我是中国人')  #此方法创建会将一个个的字拆分，比较少用，它是不能填int类型数据的
l4 = ['seo','java','python','php']  #此方法创建最为常见
l5 = '实验室设计_实验室设计报价_深圳实验室设计公司'.split('_')   #以分割的方式创建
print(l3,l4,l5)

# 列表的访问
r1 = l4[1]  #取出java
print(r1)

# 使用切片方式访问，切片的时候包含前面的索引，不包含后面的
r2 = l4[:2] #不指定，默认从第0个开始切片到 l4 的 python，下标是从0开始，切到 2 结束，也就是切 2 个
print(r2)

r3 = l4[2:3]    #从第 2 个数开始切 到第 3 个数结束，得到 python
print(r3)

# 切片步长的计算
item = ['seo','python','java','php','go','linux','c++','html']
r4 = item[::3]  #此方式的意思就是从第0个开始算到第3个结束，包含它自己，输出 seo,php,c++
print(r4)

print('-' * 50)
# 将列表进行反转
r5 = item[::-1] # -1 列表从后面开始往前面取值，写 -1 就会反转列表中的数据
print(r5)


# 二维列表的访问
lists = [[1,2,3],[4,5,6],[7,8,9]]
print(lists)

# 取123
l01 = lists[0]
print(l01)

# 取123里的 2
l011 = lists[0][1]
print(l011)


# list 列表的追加
list_1 = ['seo','python','java']
list_2 = ['php','go','linux','c++','html']

# 追加方式1
list_1.append('javascript')
print(list_1)

# 追加方式2，将 list_2 的数据追加到 list_1 中
# for x in list_2:
#     list_1.append(x)
# print(list_1)

print('*' * 50)
# 追加方式3，更简单的方法，不用写 for
# list_1.extend(list_2)   # extend 扩展的意思，将 list_2 扩展到 list_1中
# print(list_1)

# 追加方式4，使用 + 号  它会重新生成列表，而不是追加的方式
list_3 = list_1 + list_2
print(list_3)


# list 列表修改内容
u_l = ['seo','python','java']

# 以下标的方式修改，如 u_l[0] = 'c++'
u_2 = u_l[:]    #将 u_l 的列表值完全复制到 u_2 中
print(u_2)


print('删除---------------')
# list 列表删除内容
d1 = ['seo','python','java','pycharm']
#d1.pop()    #使用 .pop 进行删除，它可以指定下标，如果不指定默认删除最后一个，通常配合 for 删除，避免列表为空报错
# print(d1)

# 删除方式2
# d1.remove('python') #它删除的不是索引，是直接删除值，通常配合 if 判断会用
d1_s = 'pycharm' in d1
if d1_s:
    d1.remove('pycharm')

print(d1)