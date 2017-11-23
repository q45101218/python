#!/usr/bin/env python
# coding=utf-8

#import random

def goal(p):
    p+=10
    return p

def blast():
    print('you dead')

hp=0
while input()!='q' :
    if random.randint(1,100)%9 > 5:
        hp=goal(hp)
    else:
        blast()

print(hp)
