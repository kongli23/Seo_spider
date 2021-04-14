# -*- coding: utf-8 -*-
# 99乘法表

# 倒序
for i in range(1,10):
    for j in range(i,10):
        print(f'{j}x{i}={j*i}',end='\t')
    print()

print('-' * 50)
# 正序


x = 1
while x <= 9:
    y = 1
    while y <= x:
        print(f'{y}x{x}={y*x}',end='\t')
        y += 1
    print()
    x += 1