
# 处理标签

tags_list = []
with open('tags.txt',encoding='utf-8') as ts:
    for tag in ts:
        tag = tag.strip()+','
        tags_list.append(tag)
print(tags_list)

for tlist in tags_list:
    print(tlist.replace(',','\n'))
