# A spider to get ancient Chinese poems from gushiwen.org.
# 从 gushiwen.org 古诗文网上爬取古诗的爬虫程序。

# Fetch the title, author's name, era, content and tags of each poem, parsing them into json.
# 爬取每首诗的标题，作者，时代（朝代），内容和标签，解析为json格式。

# Notice: Up to now, access to pages after page 10 is still prohibited.
# 注意：第十页之后的页面依旧禁止访问。

import json
import random
import re
import time

import requests as req
from bs4 import BeautifulSoup as bs

poems = []
avaliable_tags = ['写景', '咏物', '春天', '夏天', '秋天', '冬天',\
    '写雨', '写雪', '写风', '写花', '梅花', '荷花', '菊花', '柳树',\
        '月亮', '山水', '写山', '写水', '长江', '黄河', '儿童', '写鸟', '写马',\
            '田园', '边塞', '抒情', '爱国', '离别', '送别', '思乡', '思念', '爱情', '励志', '哲理', '闺怨', '悼亡',\
                '写人', '老师', '母亲', '友情', '战争', '读书', '惜时', '婉约', '豪放', '民谣',\
                    '节日', '春节', '元宵节', '寒食节', '清明节', '端午节', '七夕节', '中秋节', '重阳节',\
                        '忧国忧民', '咏史怀古']

num = int(input("Input number of pages to fetch: "))

for i in range(1, num + 1):
    print("Fetching page " + str(i) + " out of " + str(num) + " page(s)...", end="")
    res = req.get("https://so.gushiwen.org/shiwen/default.aspx?page=" + str(i) + "&type=4&id=1")
    sp = bs(res.text, 'lxml')
    _poems = sp.select('div[class="main3"]')[0].select('div[class="left"]')[0].select('div[class="sons"]')
    for i in _poems:
        title = i.select('div[class="cont"]')[0].select('p')[0].select('a')[0].text
        era = i.select('p[class="source"]')[0].select('a')[0].text
        author = i.select('p[class="source"]')[0].select('a')[1].text
        content = re.sub(r"\s+", "", re.sub(r"[\(（].+[\)）]", "", i.select('div[class="cont"]')[0].select('div[class="contson"]')[0].text)).replace("\n", "")
        tags, _tags = [], i.select('div[class="tag"]')[0].select('a')
        for tag in _tags:
            if tag.text in avaliable_tags: tags.append(tag.text)
        poems.append({"title": title, "author": author, "era": era, "content": content, "tags": tags})
    print(" Done with adding " + str(len(_poems)) + " poems.")
    wait_sec = round(random.uniform(1, 4), 2)
    print("Waiting for " + str(wait_sec) + " sec...")
    time.sleep(wait_sec)

with open(r".\poems.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(poems, ensure_ascii=False, indent=4))

print("\nAll done.")
