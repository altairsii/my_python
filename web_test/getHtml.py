import urllib.request
import chardet


def getHtml(url):
    page = urllib.request.urlopen(url)
    txt = page.read()
    charset = chardet.detect(txt)
    return txt.decode(charset['encoding'])
