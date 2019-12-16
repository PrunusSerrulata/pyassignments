import requests as req
from bs4 import BeautifulSoup as bs
import re
import json

res = req.get("https://so.gushiwen.org/shiwen/default_4A111111111111A1.aspx")
sp = bs(res.text, 'lxml')
poems = sp.select('div[class="main3"]')[0].select('div[class="left"]')[0].select('div[class="sons"]')
for i in poems:
    content = i.select('div[class="cont"]')[0].select('div[class="contson"]')[0].text
    content = re.sub(r"\s+", "", re.sub(r"[\(（].+[\)）]", "", content))
    content = content.replace("\n", "")
    print(content + "\n")