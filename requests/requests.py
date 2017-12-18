#!/usr/bin/env python
# coding=utf-8
mport requests
#def getinfor (url):
#    try:
#        kv={'user-agent':'Mozilla/5.0'}
#        #r=requests.get(url)
#        r=requests.get(url,headers=kv)
#        w=requests.get(url)
#        r.raise_for_status()
#        if r.encoding is not r.apparent_encoding:
#            r.encoding=r.apparent_encoding
#            w.encoding=w.apparent_encoding
#        print((r.headers))#['user-agent'])
#        print(w.headers)
#        return r.text
#    except:
#        print("failed")
#
#url=input("input the websit that you want to get:")
#t=getinfor(url)
#print(t)


# import requests
# def search (kv):
#     try:
#         url="http://www.baidu.com/s"
#         r=requests.get(url,params=kv)
#         print(r.request.url)
#     except:
#         print("wrong")
#
# kv={}
# kv['wd']=input("what is you want to search:")
# search(kv)

# import requests
# import os
# root="E://图片//"
# def getpic (url):
#     try:
#         path=root+url.split('/')[-1]
#         if not os.path.exists(root):
#             os.mkdir(root)
#         if not os.path.exists(path):
#             r=requests.get(url)
#             f=open(path,'wb')
#             f.write(r.content)
#             f.close()
#             print("success\n")
#         else:
#             print("existed\n")
#     except:
#         print("failed")
#
# url=input("input:")
# getpic(url)

