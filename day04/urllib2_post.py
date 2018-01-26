# -*- coding: utf-8 -*-
'''
@author: Jay
@file: urllib2_post.py
@time: 2018/1/24 13:28
'''
import urllib
import urllib2

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language":"zh-CN,zh;q=0.9"
    }
key = raw_input("请输入需要翻译的文字:")
data = {'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1505653077725',
        'sign':'467d88b4cdc9c6adca72855020b6a1e8',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':'true'}
data = urllib.urlencode(data)

request = urllib2.Request(url,data=data,headers=headers)
response = urllib2.urlopen(request)

html = response.read()
print html
print type(html)
