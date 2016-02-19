# _*_ encoding:utf-8 _*_

import urllib2
import cookielib

# 保存cookie到CookieJar对象
# cookie = cookielib.CookieJar()
#
# handler = urllib2.HTTPCookieProcessor(cookie)
#
# opener = urllib2.build_opener(handler)
#
# response = opener.open("http://www.baidu.com")
#
# for item in cookie:
#     print item.name + " = " + item.value


# 保存cookie到文件

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件中获取Cookie并访问
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.baidu.com")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
