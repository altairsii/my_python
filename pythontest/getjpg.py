'''
Created on 2016年9月7日

@author: wangyongbing
'''
# ! coding=utf-8
# http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%CD%BC&fr=ala&ala=1&alatpl=others&pos=0


import re
import urllib.request

# from _io import open
 
def getHtml(url, deformat):
    page = urllib.request.urlopen(url)
    return page.read().decode(deformat)
 
def getImg(html, pythonreg):
    reg = pythonreg
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x) 
        x += 1
    return imglist
pythonurl = input('input you want Data capture url:')
print('your input url is :', pythonurl)
if pythonurl == '' :
    print('over...')
    quit()
decodetype = input('input Encoding format(gbk,utf-8...,default utf-8):')
if decodetype == '' :
    decodetype = 'utf-8'
print('your input Encoding format is :', decodetype)
pythonreg = input('input you reg for img(default r\'src="(.+?\.jpg)"\'):')
if pythonreg == '' :
    pythonreg = r'src="(.+?\.jpg)"'

html = getHtml(pythonurl, decodetype)
print(getImg(html, pythonreg))
print('end...')

