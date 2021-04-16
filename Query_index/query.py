# -*- coding: utf-8 -*-
import requests
import json

# 查询url 在收录列表的第1页（rn=0）是否存在，如果不存在则是没有收录

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76'
}
# 载入url 文件中的url 列表
for url in open('urls.txt',encoding='utf-8'):
    query_url = url.strip()
    code = requests.get(f'http://www.baidu.com/s?ie=UTF-8&wd={query_url}&tn=json&rn=0',headers=headers,timeout=30).json()

    # 提取json 中的结果
    entry = code['feed']['entry']

    # 通常结果有10个，这里只查第一条，如果存在说明已经创建了索引，如果不在第一位，说明质量低，当然没收录
    for x in entry[:1]:
        title = x.get('title')
        index_url = x.get('url')
        if query_url == index_url:
            print(f'标题：{title}|{index_url} 已收录')
        else:
            print(f'---------------{query_url} 未收录---------------')

print('检查完毕！')
