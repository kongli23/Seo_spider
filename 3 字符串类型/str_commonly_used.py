# -*- coding: utf-8 -*-
# 统计某个字符出现的次数

kw = '网站seo优化seo教程'
commonly = kw.count('seo')  #搜索字符在str中出现的次数
print(commonly)

# 判断字符串是以什么开头，以什么结尾
base_url = 'http://www.baidu.com/1.html'
r1 = base_url.startswith('https://')    #判断开头是否 https://
r2 = base_url.endswith('.html') #判断结尾是否以 .html 如果是说明它是内容页！
print(r1,r2)

html = 'dsfkj<Title>sdflkjsfsdf我是标题</title>kslkjfsd'
# 使用find提取标题
html = html.lower() #将大写转化为小写
start = html.find('<title>')    #查找指定的字符串
end = html.find('</title>')
title = html[start+7:end]    #使用切片提取 +7是算上<title>
print(title)
