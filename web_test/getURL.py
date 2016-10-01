import re
import urllib.request

"""
    This script is written for u148.

"""

filterNotHtmlreg = '(cs|xhtml|dtd|css|js)$'
filterPhoto = "(jpg|png|gif)$"


def getURL(html):
    list = []
    for geturl in getList(html):
        if re.search(filterNotHtmlreg, geturl) is not None: continue
        if geturl in list: continue
        list.append(geturl)
    return list


def getImgURL(html):
    list = []
    for geturl in getList(html):
        if re.search(filterPhoto, geturl) is None: continue
        if geturl in list: continue
        list.append(geturl)
    return list


def getURL2(html, rootPath):
    list = []
    for geturl in getList(html):
        if re.search(filterNotHtmlreg, geturl) is not None: continue
        if re.match(r'/', geturl) is not None: geturl = rootPath + geturl
        if geturl in list: continue
        list.append(geturl)
    return list


def getList(html):
    reg = '\"(/.*?|http.*?)\"'
    imgre = re.compile(reg)
    list = re.findall(imgre, html)
    return list
