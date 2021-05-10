# -*- coding: utf-8 -*-

import requests
from lxml import etree

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}

# url = 'http://www.usniuku.com/news-show-318'
# html = requests.get(headers=headers,url=url)
# el_html = etree.HTML(html.text)
# title_ = el_html.xpath('//div[@class="inside-item-content detail-content"]/h1/text()')
# content_list = el_html.xpath('//div[@class="editor"]//text()')
#
# print(title_[0])
# for content in content_list:
#     print(content)

url = 'https://www.egainnews.com/article/9870'
html = requests.get(url)
el_html = etree.HTML(html.text)
title = el_html.xpath('//h1[@class="entry-title"]/text()')
content_list = el_html.xpath('//div[@class="entry-excerpt"]//p//text()')
print(title[0])
print(''.join(content_list))    #使用join将list 组装成 str
# for content in content_list:
#     print(content)

