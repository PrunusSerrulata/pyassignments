import json
import random
import re
import time

import requests as req
from bs4 import BeautifulSoup as bs

count = -1
while count < 1:
    beg, end = map(int, input("输入要爬取诗词的序号范围, 上下界以空格分隔: ").split())
    count = end - beg + 1
    if count < 1:
        print("无效范围。\n")

mode = input("是否覆写文件?(输入Y/y为是, 其他为否): ")
rewrite = mode.lower() == "y"

f = open(r".\poems.txt", "w" if rewrite else "a", encoding="utf-8")
for poemnum in range(beg, end + 1):
    print("爬取第 " + str(poemnum) + " 号诗(" + str(poemnum - beg + 1) + " / " + str(count) + ")中...", end=" ")
    poemres = req.get("http://www.haoshiwen.org/view.php?id=" + str(poemnum))
    poemres.encoding = "utf-8"
    spr = bs(poemres.text, "lxml")
    if len(spr.select('div[class="main3"]')[0].select('div[class="shileft"]')) <= 0:
        print("该诗不存在")
        continue
    else:
        title = re.sub(r"[\f\n\r\s]", "", spr.select('div[class="main3"]')[0].select('div[class="shileft"]')[0].select('div[class="son1"]')[0].text)
        print("标题: " + title, end=" ")
        _cont, cont = spr.select('div[class="main3"]')[0].select('div[class="shileft"]')[0].select('div[class="son2"]')[0].find_all('p')[3:-1], ""
        for i in _cont:
            cont += i.text
        cont = re.sub(r"[\f\n\r\s]", "", cont)
        sents = re.split(r"[，。,.]", cont)[:-1]
        for i in sents:
            if len(i) != 5:
                valid = False
                break
            valid = True
        if valid:
            f.write(title + ":" + cont + "\n")
            print("完成")
        else:
            print("非五言诗，丢弃")
    
    if poemnum != end:
        wait_sec = round(random.uniform(1, 2), 2)
        print("等待 " + str(wait_sec) + " 秒...")
        time.sleep(wait_sec)

print("\n完成。")