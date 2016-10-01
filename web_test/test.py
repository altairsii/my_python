#!/usr/bin/python
# encoding:utf-8
from urllib.parse import quote

from web_test.getHtml import getHtml
from web_test.getImg import getImg
from web_test.getURL import getURL, getURL2
from web_test.save import saveimg, saveFile, saveFile1

html = getHtml(quote("http://www.u148.net", '/,:', 'utf-8'))  # print(html)

# saveimg(getImgURL(html), '/home/wyb/pictures/photo')

# saveimg(getURL2(html, 'http://www.u148.net'),'/home/wyb/pictures/other')
saveFile1(getURL2(html, 'http://www.u148.net'), '/home/wyb/pictures/other')

print("end")
