# _*_ encoding:utf-8 _*_

import urllib2
import urllib

# values = {"username": "name", "password": "pwd"}
# data = urllib.urlencode(values)
# print(data)
#
# httpHander = urllib2.HTTPHandler(debuglevel=1)
# httpsHander = urllib2.HTTPHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHander,httpsHander)
# urllib2.install_opener(opener)
# request = urllib2.Request("http://www.baidu.com")
# reponse = urllib2.urlopen(request)
# print reponse.read()

request = urllib2.Request("http://www.wwwxxxxxxxwww.com")

try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print(e.reason)
