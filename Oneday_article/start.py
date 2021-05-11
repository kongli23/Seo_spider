# -*- coding: utf-8 -*-
import requests
import json
import cchardet
import extractor
from threading import Thread
from queue import Queue

# query = f'https://www.baidu.com/s?ie=UTF-8&wd={kw}&tn=json&rn=50' 50条json链接
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=摄影灯&rsv_enter=1&rsv_dl=tb&gpc=stf=1620128867,1620733667|stftype=1&tfflag=1  一周的参数链接
# https://www.baidu.com/s?ie=UTF-8&wd=摄影灯&tn=json&rn=50&rsv_enter=1&rsv_dl=tb&gpc=stf=1620128867,1620733667|stftype=1&tfflag=1  50条json的一周参数链接

class Spider_url(Thread):
    '''
    采集一天最新的url链接
    '''
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

    def __init__(self,queue_urllist,queue_download_url):
        super(Spider_url, self).__init__()
        self.queue_urllist = queue_urllist
        self.queue_download_url = queue_download_url

    def run(self):
        while True:
            try:
                url = self.queue_urllist.get()
                source = self.download(url)

                # 判断返回的源码是否字符串，如果是则说明被检测了
                if isinstance(source,str):
                    print(f'被百度识别了....')

                    # 检测到被识别之后再次将关键词放入队列中查询
                    self.queue_urllist.put(url)
                    continue
            except AttributeError:
                continue
            else:
                if isinstance(source,dict):
                    self.parse_html(source)
                else:
                    continue
            finally:
                self.queue_urllist.task_done()

    def parse_html(self,source):
        '''
        解析json源码中的url 并过滤某些网站，处理完毕存入列队中
        :param source: 传入json源码数据
        :return:
        '''

        feed = source.get('feed',{})
        entry = feed.get('entry',[])

        for item in entry[:-1]:
            title = item.get('title','')
            url = item.get('url','')

            # print(title+'|'+url)
            self.queue_download_url.put((title,url))

    def download(self,url):
        '''
        下载源码函数
        :param url:传入url
        :return: 返回json数据源码
        '''
        query = url
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

class Download_article(Thread):
    '''
    根据 url 地址采集文章
    '''

    # headers = {
    #     'User-Agent':'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
    # }
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
        'User-Agent':'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
    }

    def __init__(self,queue_download):
        super(Download_article, self).__init__()
        self.queue_download = queue_download

    def run(self):
        while True:
            try:
                title,url = self.queue_download.get()

                # 开始下载文章源码
                source = self.download(url)
                if source is None:
                    continue

                self.extract_content(url,source)
            finally:
                self.queue_download.task_done()

    def download(self,url,retrys=3):
        '''
        下载文章源码
        :param url:
        :return:
        '''

        try:
            resp = requests.get(url, headers=self.headers, timeout=15)
        except requests.RequestException as err:
            html = None
            print('{}:下载文章异常：{}'.format(url, err))

            if retrys > 0:
                return self.download(url,retrys -1)
        else:
            text = resp.content  # 这里返回的是二进制的内容
            encoding = cchardet.detect(text)['encoding']
            if encoding is None:
                encoding = 'utf-8'
            html = text.decode(encoding=encoding, errors='ignore')
        return html

    def extract_content(self,url,source):
        '''
        提取文章正文
        :param kw: 关键词
        :param url: 文章的地址
        :param source: 正文代码段
        :return:
        '''
        ex = extractor.Extractor()
        ex.extract(url,source)

        # 过滤文章,质量不少于10000分, 并且字数超过5000的不要(字数太多,翻译容易出错)
        if ex.score > 10000 and ex.text_count < 5000:
            title = ex.title.replace('/','')
            content = ex.format_text    #带源码的内容
            with open(f'article\\{title}.html','w',encoding='utf-8') as wt:
                wt.write(content+f'\n\n\n\n下载地址：{url}')

if __name__ == '__main__':
    queue_urllist = Queue()
    queue_download_url = Queue()

    keywords = '摄影灯'
    for i in range(0,2):
        # 第一页
        url = f'https://www.baidu.com/s?ie=UTF-8&wd={keywords}&tn=json&rn=50&rsv_enter=1&rsv_dl=tb&gpc=stf=1620654861,1620741261|stftype=1&tfflag=1'
        # 第二页
        if i == 1:
            url = f'https://www.baidu.com/s?ie=UTF-8&wd={keywords}&tn=json&rn=50&pn=50&rsv_enter=1&rsv_dl=tb&gpc=stf=1620654861,1620741261|stftype=1&tfflag=1'
        queue_urllist.put(url)

    # 加载过滤url
    filter_url = []
    for k in open('filter_url.txt', encoding='utf-8'):
        filter_url.append(k.strip())

    # 采集一天最新url
    for x in range(2):
        spider = Spider_url(queue_urllist,queue_download_url)
        spider.daemon = True
        spider.start()

    # 下载一天最新文章
    for d in range(5):
        download = Download_article(queue_download_url)
        download.daemon = True
        download.start()

    queue_urllist.join()
    print('采集完毕！')

    queue_download_url.join()
    print('下载完毕！')