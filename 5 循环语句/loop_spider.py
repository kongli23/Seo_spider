# -*- coding: utf-8 -*-
import requests

# 使用 for 批量采集网页内容
# http://www.guihuashujiage.com/guihuaxixing/471.html

for n in range(30):
    url = f'http://www.guihuashujiage.com/guihuaxixing/4{n}.html'
    code = requests.get(url)
    code.encoding = 'utf-8'
    str_code = code.text
    title = str_code[str_code.find('<h1 class="post-title">')+23:str_code.find('</h1')]

    content = str_code[str_code.find('<div class="entry">'):str_code.find('<div class="tags">')]
    print(title)
    print(content)
    print('=' * 50)