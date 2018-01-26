# -*- coding: utf-8 -*-
'''
@author: Jay
@file: tieba.py
@time: 2018/1/23 21:33
'''
import urllib
import urllib2
from lxml import etree

def loadPage(url):
    """
    
    :param url: 
    :return: 
    """
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(request).read()
    html = html.replace("<!--","").replace("-->","")
    # with open("tieba.html","wb") as f:
    #     f.write(html)
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(html,parser=None)
    # content = etree.fromstring(html)
    #print content
    # 返回所有匹配成功的列表集合
    # link_list = content.xpath('//div[@class="t_con cleafix"]//div/a/@href')
    # link_list = content.xpath('//li[@class="j_thread_list clearfix"]/div/div/div/div/a/@href')
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    #link_list = content.xpath('//a[@class="j_th_tit"]/@href')
    for link in link_list:
        # print link
        fulllink = "http://tieba.baidu.com" + link
        # 组合为每个帖子的链接
        #print link
        loadImage(fulllink)
def loadImage(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)"
    }
    request = urllib2.Request(link, headers=headers)
    # 获取每个帖子连接
    html = urllib2.urlopen(request).read()
    # 解析html文档
    re_xml = etree.HTML(html,parser=None)
    # 返回忧图片链接的集合
    link_list = re_xml.xpath('//div[@class="d_post_content j_d_post_content "]//img[@class="BDE_Image"]/@src')

    for link in link_list:
        # print link
        writeImage(link)
def writeImage(link):
    """
         将html文件写入本地
         html 响应文件内容: 
         filename:文件名字
    """
    # print "正在保存"+filename
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)"
    }
    request = urllib2.Request(link, headers=headers)
    image = urllib2.urlopen(request).read()
    filename = link[-10:]
    with open(filename,"wb") as f:
        f.write(image)
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
        fullurl = url + "&pn=" + str(pn)
        loadPage(fullurl)
        # print e_link
        # loadImage(e_link)

if __name__ == '__main__':
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)

