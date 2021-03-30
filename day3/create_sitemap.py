# -*- coding: utf-8 -*-

# <?xml version="1.0" encoding="UTF-8"?>
# <urlset>
# <!-- urlset，urlset用来标记整个文档的开头，最少出现1次 最多出现1次 -->
#     <url>
#     <!-- url，url标记每条信息的开始和结束，最少出现0次 最多出现50000次 -->
#         <loc>http://www.baidu.com/</loc>
#         <!-- loc，该条数据的存放地址，最少出现1次 最多出现1次，类型为URL地址，最小长度1个字符 最大长度256个字符 必须符合正则表达式(http://)(.+) -->
#         <lastmod>2013-01-01</lastmod>
#         <!-- lastmod，指该条数据的最新一次更新时间，最少出现0次 最多出现1次，类型为日期或日期时间，格式为YYYY-MM-DD的日期或者格式为YYYY-MM-DDThh:mm:ss的日期时间（请注意日期与时间之间以“T”分隔） -->
#         <changefreq>always</changefreq>
#         <!-- changefreq，指该条数据的更新频率，最少出现0次 最多出现1次，类型为字符串，有效值为：always、hourly、daily、weekly、monthly、yearly、never -->
#         <priority>1.0</priority>
#         <!-- priority，用来指定此链接相对于其他链接的优先权比值，此值定于0.0-1.0之间，最少出现0次 最多出现1次，类型为小数，最小值为（包含）0.0 最大值为（包含）1.0 -->
#     </url>
# </urlset>

import time
url = ''
for i in range(100):
    url_list = """
    <url>
        <loc>http://www.baidu.com/{}.html</loc>
        <lastmod>{}</lastmod>
        <changefreq>always</changefreq>
        <priority>1.0</priority>
    </url>
    """.format(i,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    url += url_list


temp = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset>
    {}
</urlset>
""".format(url)
print(temp)

