'''
Created on 2016年9月7日

@author: wangyongbing
'''
# ! coding=utf-8
# http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%CD%BC&fr=ala&ala=1&alatpl=others&pos=0


import re
import urllib.request
# from _io import open
 
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('gbk')
    return html
 
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x) 
        x += 1
    return imglist

 
html = getHtml("http://www.3lian.com/gif/2015/04-06/79269.html")
print(getImg(html))


