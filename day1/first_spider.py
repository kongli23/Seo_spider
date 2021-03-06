#! -*- coding: utf-8 -*-
'''
第一个爬虫
'''

import requests #引入专用的爬虫程序包
html = requests.get('https://www.baidu.com')    #请求网页url数据
html.encoding = 'utf-8' #设置编码格式
print(html.text)    #输出数据