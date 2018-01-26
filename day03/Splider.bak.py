#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Jay
@file: Splider.py
@time: 2018/1/23 13:57
'''
import urllib2
url = "http://www.baidu.com"
# 向指定的url地址发送请求 返回服务器相应的对象
response = urllib2.urlopen(url)
# read()读取文件全部内容
res = response.read().encode()
print res




