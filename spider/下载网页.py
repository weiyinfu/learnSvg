import requests

resp = requests.get("https://www.w3school.com.cn/svg/svg_examples.asp")
resp.encoding = 'gbk'
open("index.html",'w').write(resp.text)
