# -*- coding: utf-8 -*-
# 循环语句

sum = 1
while sum <= 10:
    print('第{}遍'.format(sum))
    sum +=1 # 等同于    sum = sum+1，每循环一次+1，不然会一直条件不满足死循环

# 使用 while 生成0-10的url
page = 0
while True:
    if page >=10:
        break
    print(f'http://www.baidu.com/seo/{page}.html')
    page +=1

# 使用while打印 99 乘法表，正序
x = 1
while x <= 9:
    y = 1
    while y <= x:
        print(f'{y}x{x}={y*x}',end='\t')
        y += 1
    print()
    x += 1

# 使用while打印 99 乘法表，倒序
