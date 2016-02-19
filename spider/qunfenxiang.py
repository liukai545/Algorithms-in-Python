# _*_ encoding:utf-8 _*_

import urllib
import urllib2
import re
import Tool
import time
from threadpool import ThreadPool, makeRequests

"""
只找最新的第一页
"""


class MainBar:
    def __init__(self):
        self.tool = Tool.Tool()
        self.links = set([])

        pass

    def getPage(self, url):
        try:
            request = urllib2.Request(url)
            reponse = urllib2.urlopen(request)
            return reponse.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接贴吧失败，错误原因", e.reason
                return None

    def getTitleList(self, page):
        str = '<div class="threadlist_title pull_left j_th_tit ">.*?<a href="(.*?)".*?>(.*?)</a>'
        pattern = re.compile(str, re.S)
        items = re.finditer(pattern, page)
        linksTitleDict = {}
        for item in items:
            linksTitleDict['http://tieba.baidu.com' + item.group(1)] = item.group(2)
            print item.group(2) + '  ' + item.group(1)
        return linksTitleDict

    def getHomePageList(self, articleLink):
        print('prasing link : ' + articleLink)
        page = self.getPage(articleLink)
        str = '<div id="post_content_.*?>(.*?)</div>'
        pattern = re.compile(str)
        items = re.findall(pattern, page)

        for item in items:
            set = self.__extractHomePageLink(self.tool.replace(item))
            self.links = self.links | set

    def __extractHomePageLink(self, str):
        strre = '(short=\w{7})'
        compile = re.compile(strre, re.S)
        lists = compile.findall(str)
        links = set([])
        for i in lists:
            link = ('http://pan.baidu.com/mbox/homepage?' + i)
            links.add(link)
            print('find homepage link : ' + link)
        return links

    def run(self):

        page = self.getPage(baseURL)
        linksTitleDict = self.getTitleList(page)

        # for i, link in enumerate(articleLinks):
        #     print('parsing links in title: ' + articleTitle[i])
        #     links = self.getHomePageList(link)

        pool = ThreadPool(10)

        requests = makeRequests(self.getHomePageList, linksTitleDict.keys())
        #[pool.putRequest(req) for req in requests]
        for req in requests:
            pool.putRequest(req)
            print(req)
        pool.wait()

        for link in self.links:
            print(link)


baseURL = 'http://tieba.baidu.com/f?kw=%E9%AB%98%E6%B8%85%E7%94%B5%E5%BD%B1%E8%B5%84%E6%BA%90&ie=utf-8'
mainbar = MainBar()


def timer(n):
    while True:
        print time.strftime('%Y-%m-%d %X', time.localtime())
        old = mainbar.links
        mainbar.run()
        cha = mainbar.links - old
        print(cha)
        time.sleep(n)


if __name__ == '__main__':
    timer(5)
