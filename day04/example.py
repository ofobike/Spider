# -*- coding: utf-8 -*-
'''
@author: Jay
@file: example.py
@time: 2018/1/23 20:21
'''
import urllib

name = raw_input("输入姓名:")
result_dict = {
    "wd":"杨少杰"
}
get_result = urllib.urlencode(result_dict)
print get_result