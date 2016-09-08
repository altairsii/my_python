'''
Created on 2016年9月6日

@author: wangyongbing
'''
from pythontest import fibo
from _io import open

# a=[1,1,2,3,34.5,6]
# print(a.count(1),a.count(34.5),a.count("X"))
# a.insert(2,-1)
# a.append(99)
# print(a)
# 
# print(a.index(3))
# print(a.pop())
# 
# print(a)
# 
# from math import pi
# print([str(round(pi, i)) for i in range(1, 50)])
# 
# matrix=[
#     [1,2,3],    
#     [4,5,6],
#     [7,8,9],
#     [10,11,12],
#     ]
# print(list(zip(*matrix)))
# 
# print(fibo.fib(1000))

print(fibo.__name__)
f = open('thisPython', 'w')
f.write('dddddddddd')
f.close()
