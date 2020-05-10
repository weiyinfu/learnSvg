import re

s = open("index.html").read()
res = re.findall("<a.*svg.*</a>", s)
print(res)
folder = "../demo"
import requests
import os
import json
from os.path import *

if not os.path.exists(folder):
    os.mkdir(folder)
index = []
for item in res:
    x = re.search("<a.*href=\"(.+?)\".*>(.+)</a>", item)
    url, title = x.group(1), x.group(2)
    if not url.endswith(".svg"): continue
    filename = join(folder, title + ".svg")
    index.append(relpath(filename, ".."))
    if exists(filename):
        continue
    title = re.sub("\s", "", title, )
    if not url.startswith("/"):
        url = '/' + url
    if not url.startswith("/svg"):
        url = "/svg" + url
    url = f"https://www.w3school.com.cn{url}"
    resp = requests.get(url)
    resp.encoding = 'utf8'
    content = resp.text
    print(url, title)
    open(filename, "w").write(content)
json.dump(index, open("../demo/index.json", 'w'), ensure_ascii=0, indent=2)
