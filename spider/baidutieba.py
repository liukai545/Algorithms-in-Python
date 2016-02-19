# _*_ encoding:utf-8 _*_
import urllib
import urllib2
import re
import Tool


class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool.Tool()

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            reponse = urllib2.urlopen(request)
            return reponse.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接贴吧失败，错误原因", e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        str = '<h3 class="core_title_txt.*?>(.*?)</h3>'
        pattern = re.compile(str)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group(1)
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        str = '<li class="l_reply_num.*?</span>.*?>(.*?)</span>'
        pattern = re.compile(str)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group(1)
        else:
            return None

    def getContent(self,page):
        str = '<div id="post_content_.*?>(.*?)</div>'
        pattern = re.compile(str)
        items = re.findall(pattern, page)

        for item in items:
            print self.tool.replace(item)
            print('=====================================================')

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
page = bdtb.getPage(1)
bdtb.getTitle()
bdtb.getPageNum()
bdtb.getContent(page)
