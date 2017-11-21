#!/usr/bin/env python
# coding=utf-8


"""
open file
check information
"""
import os
count=0 

while count<3:
    if os.path.isfile('log.md'):
        print("locked")
        break
    username=input("name:")
    passwd=input("password:")
    if username=='play01' and passwd=='123':
        print('success')
        break
    else:
        count+=1
        print('fail')
        if count==3:
            open('log.md','w').write(username)

