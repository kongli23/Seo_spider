# -*- coding: utf-8 -*-
# list 列表排序

list1 = [4,3,5,1,6,8,9,0]
# list1.sort()    #排序，从小到大
# print(list1)

# list1.sort(reverse=True)    #从大到小
# print(list1)

# 其它操作，例如 相乘
list2 = list1 * 3
print(list2)

# 判断某个值在不在列表中，如下，判断6 不存在列表 list2 中则返回 True
is_str = 6 not in list2
print(is_str)

# 判断某个字符出现的次数
str_count = list2.count(5)
print(str_count)

# 判断返回下标
str_index = list2.index(4)
print(str_index)

# 列表推导式练习
# 下方结果是 for 的简写，其中 x 是不变的 format 的 x 可以任意相加乘，此写法能省很多代码
url_list = ['http://www.baidu.com/seo/{}.html'.format(x) for x in range(1,50)]
print(url_list)

sum_list = [3,4,5,6,1,8,3]
s_s = sum(sum_list)
print(s_s)