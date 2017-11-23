#!/usr/bin/env python
# coding=utf-8

import random

f=open("./t.md",'a+')
for i in range(1,100):
    str1=str(random.random())
    f.write(str1+"\n")
f.close()


