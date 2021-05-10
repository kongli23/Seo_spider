# -*- coding: utf-8 -*-

# 元组常用操作
# 赋值的时候只要用逗号隔开赋值就是元组，如下
sum_list = 1,2,3,4,5,6
print(sum_list,type(sum_list))

# 元组的解包
url_info = ('http://www.baidu.com','百度一下你就知道','是否收录','2021-04-12 23:55')
url,title,is_index,index_time = url_info
print(url,title,is_index,index_time)

