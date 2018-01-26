#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Jay
@file: Splider.py
@time: 2018/1/23 13:57
'''
import urllib2

url = "http://www.baidu.com/"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
# 构造请求对象
resquest = urllib2.Request(url,headers=headers)
# 向指定的url地址发送请求 返回服务器相应的对象
response = urllib2.urlopen(resquest)
# read()读取文件全部内容
res = response.read()
# 返回响应码
status = response.getcode()
# 获得实际页面的url
html_url = response.geturl()
# 返回响应的信息
html_info = response.info()
print res
print status
print html_url
print html_info




