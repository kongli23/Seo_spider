# -*- coding: utf-8 -*-
'''
查询url收录类
'''
import requests
import json
from threading import Thread
from queue import Queue

class Baidu_query(Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
    }
    def __init__(self,queue_urllist):
        super(Baidu_query, self).__init__()
        self.queue_urllist = queue_urllist

    def run(self):
        while True:
            try:
                kw = self.queue_urllist.get()
                source = self.download(kw)

                # 判断返回的源码是否字符串，如果是则说明被检测了
                if isinstance(source,str):
                    print('被百度识别了....')
                    continue
                self.parse_html(kw,source)

            finally:
                self.queue_urllist.task_done()

    def parse_html(self,kw,source):
        feed = source.get('feed',{})
        entry = feed.get('entry',[])
        for item in entry[:-1]:
            title = item.get('title','')
            url = item.get('url','')
            if url == kw:
                print(f'{title}\t{url}\t已收录\n')

    def download(self,url):
        query = f'http://www.baidu.com/s?ie=UTF-8&wd={url}&tn=json&rn=10'
        try:
            code = requests.get(query,headers=self.headers,timeout=15)
        except requests.RequestException as err:
            print(f'下载异常：{err}')
        else:
            code.encoding = 'utf-8'
            try:
                return code.json()
            except json.JSONDecodeError:
                return code.text

if __name__ == '__main__':
    queue_urllist = Queue()

    # 载入待查询的url
    with open('urls.txt',encoding='utf-8') as f:
        for x in f:
            queue_urllist.put(x.strip())

    # 开两个线程查询
    for x in range(2):
        baidu = Baidu_query(queue_urllist)
        baidu.daemon = True
        baidu.start()

    queue_urllist.join()
    print('查询结束！')