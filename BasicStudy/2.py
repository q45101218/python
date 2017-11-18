#!/usr/bin/env python
# coding=utf-8

Sum=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        Sum.append(i)
print(sum(Sum))

