import requests
from lxml import etree
url = 'https://https://dldl1.815322.xyz/xiaoshuo/5/5067.html'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
rep = requests.get(url,headers=headers)
rep.encoding = 'utf-8'
##print(rep.text)
e=etree.HTML(rep.text)
info = '\n'.joine(e.xpath('//div[@class="m-post"]/p/text()'))
title = e.xpath('//div[@class="entry-tit"]/h1/text()')[0]
url = e.xpath('//table/tbody/tr/td[2]/a/@href')
print(info)
print(title)
with open("斗罗大陆.txt",'w',encoding = 'utf-8')as f:
    f.write(title+'\n'+info+'\n')
