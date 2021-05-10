# -*- coding: utf-8 -*-

# 字典练习

site = {
    'domain':'www.baidu.com',   #域名
    'article_num':100000,   #文章总数量
    'keywords':['seo','seo是什么','seo优化','seo教程','python','python爬虫','python seo','网站优化'], #排名关键词
    'baidu':{
        'index':1000,   #百度收录
        'keywords':['seo','seo是什么','seo优化','seo教程','python'],   #百度排名词
        'daily':300 #日收录量
    },
    'sogou':{
        'index':200,
        'keywords':['python爬虫','python seo','网站优化'],
        'daily':4
    }
}

print(site)

# 获取百度里的内容
baidu = site['baidu']['index']  #有几层就写几个键
print(baidu)

# 获取搜狗里面的内容
sogou = site.get('sogou',{}).get('keywords',[]) #后面的 {} 代表它是字典，[] 代表是集合，为了防止错误，设置默认的报错为相同类型
print(sogou)

# 向里面添加数据
site['baidu']['uv'] = 1546
print(site)