#!/usr/bin/env python
# coding=utf-8

name=input("Please input your name:")
if name =='':
    name="player 1"
hp=100
mp=100

hero=[name,hp,mp]
print("hero's name:",hero[0],"hp:",hero[1],"mp:",hero[2])

