# -*- coding: utf-8 -*-
'''
查询url收录类
'''
import requests
import json
from threading import Thread
from queue import Queue
import user_agent

class Baidu_query(Thread):

    def __init__(self,queue_urllist,domain):
        super(Baidu_query, self).__init__()
        self.queue_urllist = queue_urllist
        self.domain = domain

    def run(self):
        while True:
            try:
                kw = self.queue_urllist.get()
                # print(f'正在查询关键词：{kw}')
                source = self.download(kw)

                # 判断返回的源码是否字符串，如果是则说明被检测了
                if isinstance(source,str):
                    print(f'被百度识别了....{source}')
                    continue
                self.parse_html(kw,source)

            finally:
                self.queue_urllist.task_done()

    def parse_html(self,kw,source):
        feed = source.get('feed',{})
        entry = feed.get('entry',[])

        is_rank = dict()
        for item in entry[:-1]:
            title = item.get('title','')
            url = item.get('url','')
            pn = item.get('pn','')

            if self.domain in url:
                is_rank['title'] = title
                is_rank['url'] = url
                is_rank['pn'] = pn
                is_rank['kw'] = kw
                print(f'标题：{title}\t链接：{url}，当前排名：{pn}，关键词：{kw}')
        print('*' * 50)
        if kw not in is_rank.get('kw',''):
            print(f'{kw}-----无排名')

    def download(self,kw):
        query = f'http://www.baidu.com/s?ie=UTF-8&wd={kw}&tn=json&rn=50'
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
        # print(f'当前ua：{headers}')
        try:
            code = requests.get(query,headers=headers,timeout=15)
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
    with open('keys.txt',encoding='utf-8') as f:
        for x in f:
            queue_urllist.put(x.strip())

    domain = 'sellertop.com'
    # 开两个线程查询
    for x in range(2):
        baidu = Baidu_query(queue_urllist,domain)
        baidu.daemon = True
        baidu.start()

    queue_urllist.join()
    print('查询结束！')