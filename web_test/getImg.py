import re
import urllib.request


def getImg(html):
    reg = r'src="(.+?)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1
    return imglist
