#!/usr/bin/python
# -*- coding: utf-8 -*-
import traceback
import urllib.request
import hashlib
import os
import sys
from urllib.parse import quote


def saveimg(list, filepath):
    chickPath(filepath)
    for url in list:
        suffix = os.path.splitext(url)[1]
        print(suffix)
        filename = hashlib.sha224(str(url).encode('utf-8')).hexdigest()
        urllib.request.urlretrieve(url, filename + suffix)
    return


def saveFile(list, filepath):
    chickPath(filepath)
    for url in list:
        urllib.request.urlretrieve(url, os.path.basename(url))
    return


def saveFile1(list, filepath):
    chickPath(filepath)
    for url in list:
        filename = str(os.path.basename(url))
        print(url, 'a==', filename)
        if filename == "" or filename == b'' or len(filename) < 5: filename = str(url).replace("/", ".")
        print(url, '==', filename, '===', sys.getdefaultencoding())
        try:
            urllib.request.urlretrieve(quote(url, '/,:', 'utf-8'), filename)
        except Exception:
            print(traceback.format_exc(), url)

    return


def chickPath(filepath):
    if filepath is None: return
    if os.path.isdir(filepath) == False:
        os.mkdir(filepath)
    os.chdir(filepath)


def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)
