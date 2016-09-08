'''
Created on 2016年9月8日

@author: wangyongbing
'''
import hashlib
m=hashlib.md5()
m.update('no zuo no die'.encode(encoding='utf_8', errors='strict'))
print(m.digest())
print(hashlib.sha224("http://img15.3lian.com/2015/f1/127/56.jpg".encode('utf-8')).hexdigest())
hashtxt=hashlib.sha224("this is a hash code test.".encode('utf-8')).hexdigest()
for i in range(0,len(hashtxt)):
    print(chr(ord(hashtxt[i])))
# print(hashtxt)
# print(hashtxt^(hashtxt>>16))
print(int(bin(10).replace('0b',''))<<2)
