#!/usr/bin/env python
# coding=utf-8
 

import random
str1=[1,23,4,5,6,7]
print(len(str1))

r=[]
#x='xwdfdsfs'
for i in range(1,200):
    r.append(chr(random.randint(1,256)))

print(r)
