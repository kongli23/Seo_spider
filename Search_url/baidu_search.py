# -*- coding: utf-8 -*-
import requests
from lxml import etree
from threading import Thread
from queue import Queue

class Search_baidu(Thread):
    def __init__(self,queue_url):
        super(Search_baidu, self).__init__()
        self.queue_url = queue_url

    def run(self):
        while True:
            pass

if __name__ == '__main__':
    queue_url = Queue()


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
    # 'User-Agent': user_agent.get_ua()
}

k_list = [x.strip() for x in open('keys.txt',encoding='utf-8')]
for k in k_list:

    pp = 0
    info = {}
    url = []
    for i in range(0,10):
        query = f'https://www.baidu.com/s?wd={k}&pn={pp}'
        # url.append((k,f'https://www.baidu.com/s?wd={k}&pn={pp}'))
        temp_html = requests.get(query,headers=headers,timeout=15)
        el_html = etree.HTML((temp_html.text))
        snapshot_url = el_html.xpath('//h3/a/@href')

        for url_item in snapshot_url:
            str_url = str(url_item) #防止lxml占用过多内存，转为字符串防止整个树被回收
            str_url = str_url.replace('http://', 'https://')
            queue_url.put((k,str_url))
            # url.append((k,url_item))
        pp = pp+10

    # print('-' * 50)
    # for u in url:
    #     key,url = u
    #     print(f'关键词：{key}，url：{url}')
print('初始化完成...准备查询排名')