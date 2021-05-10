# -*- coding: utf-8 -*-

# 所有的不可变类型都是可以哈希的，它有什么用，意思是不可以被哈希的类型不能做为键使用
h = hash('你好')   #会将hello 转化成哈希值
print(h)

# 字典，它通常用来解析网站里的 JSON 数据，因为　JSON 数据与字典一样
d1 = dict()
print(d1)

# 常用字典创建
site = {
    'domain':'www.baidu.com',
    'index_num':100000,
    'keywords_num':2000
}
print(site)

# 根据键取值
domain = site['domain']
print(domain)

# 使用 get 获取，传入键名，如果获取不到会返回None，此方式更安全，不会报错
index_num = site.get('index_num')
# index_num = site.get('index_numd',0) #它可以设置显示默认值为 0 或者其它
print(index_num)

# 向字典添加数据，新增与修改都是用此方法，如果键名不存在则会创建，存在则会修改
site['uv'] = 100000
print(site)