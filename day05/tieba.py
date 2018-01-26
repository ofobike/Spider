# -*- coding: utf-8 -*-
'''
@author: Jay
@file: tieba.py
@time: 2018/1/23 21:33
'''
import urllib
import urllib2

def loadPage(url,filename):
    """
        根据url请求，获取服务器响应文件
        url:需要爬取得url地址
        filename:文件名字
    """
    print "正在下载" +filename
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)"
    }
    request = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(request).read()
    # print html
    return html


def writePage(html,filename):
    """
         将html文件写入本地
         html 响应文件内容: 
         filename:文件名字
    """
    print "正在保存"+filename
    with open(filename,"wb") as f:
        f.write(html)
    print "-"*30

# 主程序
def tiebaSpider(url,beginPage,endPage):
    """
        贴吧爬虫调度器
        url:贴吧url的前部分
        beginPage:起始页
        endPage:结束页
    """
    for page in range(beginPage,endPage+1):
        pn = (page -1)*50
        filename = "第"+str(page)+"页.html"
        full_url = url + "&pn=" + str(pn)
        # print full_url
        html = loadPage(full_url,filename)
        # 保存在本地
        writePage(html,filename)

if __name__ == '__main__':
    kw = raw_input("请输入需要爬取得贴吧名字:")
    beginPage = int(raw_input("请输入起始页:"))
    endPage = int(raw_input("请输入结束页"))


    url = "https://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)

