'''
Created on 2016年9月7日

@author: wangyongbing
'''
# ! coding=utf-8
# http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%CD%BC&fr=ala&ala=1&alatpl=others&pos=0


import re
import urllib.request
import chardet
import hashlib

 
def getHtml(url):
    page = urllib.request.urlopen(url)
    body = page.read()
    encodings = chardet.detect(body)['encoding'];
    print(encodings)
    return body.decode(encodings)
 
def getImg(html, pythonreg, filepath):
    reg = pythonreg
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        filename = hashlib.sha224(str(imgurl).encode('utf-8')).hexdigest()
        urllib.request.urlretrieve(imgurl, filepath + filename + '%s.jpg' % x) 
        x += 1
    return imglist
pythonurl = input('input you want Data capture url:')
print('your input url is :', pythonurl)
if pythonurl == '' :
    print('over...')
    quit()

pythonreg = input('input you reg for img(default r\'src="(.+?\.jpg)"\'):')
if pythonreg == '' :
    pythonreg = r'src="(.+?\.jpg)"'
filepath = input('input you want save path:')
html = getHtml(pythonurl)
print(html)
print(getImg(html, pythonreg, filepath))
print('end...')

