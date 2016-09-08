'''
Created on 2016年9月7日

@author: wangyongbing
'''
from pipes import Template

# from urllib.request import urlopen
# 
# 
# with urlopen('http://www.baidu.com') as response:
#     for line in response:
#         line = line.decode('utf-8')
#         if 'title' in line or 'EDT' in line:
#             print(line)


# from datetime import  date
# 
# now = date.today()
# print(now)
# print(now.strftime('%m-%d-%y.%d %b %Y is a %A on the %d day of %B'))
# birthday=date(1989,10,17)
# age=now-birthday
# print(age.days)

# import zlib
# s=b'witch which has which witches wrist watch'
# print(len(s))
# t=zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))

# from timeit import  Timer
# print(Timer('t=a;a=b;b=t','a=1;b=2').timeit())
# print(Timer('a,b=b,a','a=1;b=2').timeit())


# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#     >>> print(average([20,30,70]))
#     40.0
#     """
#     return sum(values)/len(values)
# import doctest
# print(doctest.testmod())

# import reprlib
# print(reprlib.repr(set('supercaalifragilisticexpialidocious')))

# import  pprint
# t=[[[['black','cyan'],'white',['green','red']],[['magenta','yellow'],'blue']]]
# pprint.pprint(t,width=30)

# import textwrap
# doc="""The wrap() method is just like fill() except that it returns
#  a list of strings instead of one big string with newlines to separate
#  the wrapped lines.
#  """
# print(textwrap.fill(doc, width=40))

# import locale
# print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
# conv=locale.localeconv()
# x=1234567.8
# print(locale.format("%d", x, grouping=True))
# print(locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'],x),grouping=True))

# from string import Template
# t=Template('${village}folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham',cause='the ditch fund'))
# 
# t=Template('Return the $item to $owner.')
# d=dict(item='unladen swallow')
# print(t.substitute(d))
# print(t.safe_substitute(d))


import time,os.path
photofiles=['img_1074.jpg','img_1076.jpg']
class BatchRename(Template):
    delimiter='%'
fmt=input('Enter rename style(%d-date %n-seqnum %f-format): ')
t=BatchRename(fmt)
date=time.strftime('%d%b%y')
for i,filename in enumerate(photofiles):
    base,ext= os.path.splitext(filename)
    newname=t.substitute(d=date,n=i,f=ext)
    print('{0}-->{1}'.format(*filename, newname))












