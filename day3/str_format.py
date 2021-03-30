# -*- coding: utf-8 -*-

# %s %d 格式化的用法
# %% 代表 %
address = ['深圳','广州','东莞','上海','江苏','湖南']
jobs = ['seo','python','运营','linux运维']
for a in address:
    for j in jobs:
        job = '%s%s招聘' % (a,j)
        print(job)


# 格式化2
str = '{0}价格_{0}批发_{0}厂家'.format('小米')  #括号里的 0 表格重复format的第几个数据
print(str)