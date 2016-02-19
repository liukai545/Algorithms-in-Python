# _*_ encoding:utf-8 _*_

# import re
# str = '谁有，发一个呗，谢谢啦直降200  魅族MX5新' \
#       '春特惠售1499元起http://pan.baidu.com/mbox/homepage?short=gd1smaR  无效就复制粘贴到别的帖子里http://pan.baidu.com/mbox/' \
#       'homepage?short=gd1smaR 无效就复制粘贴到别的帖子里http://pan.baidu.com/mbox/homepage?short=gd1smaR 无效就复制粘贴到' \
#       '别的帖子里http://pan.baidu.com/mbox/homepage?short=gd1smaR 无效就复制粘贴到别的帖子里http://pan.baidu.com/mb' \
#       'ox/homepage?short=gd1smaR  无效就复制粘贴到别的帖子里http://pan.baidu.com/mbox/homepage?short=c0xz6gC  链接失效了就复制到别的群里点' \
#       '一下就可以了。http://pan.baidu.com/mbox/homepage?short=c0xz6gC  链接失效了' \
#       '就复制到别的群里点一下就可以了。加我百度云http://pan.baidu.com/mbox/homepage?short=c0xz6gC  链接失效了就' \
#       '复制到别的群里点一下就可以了。撸主，呼叫撸主。链接没效果呐加我wy-19960525关键我有资源呀'
#
# strre = '(short=\w{7})'
#
# compile = re.compile(strre,re.S)
#
# lists = compile.findall(str)
#
# for i in lists:
#     print(i)

#!/usr/bin/env python
#-- encoding:utf-8 --


old  = set([1,2,3])

old_bak = old

new  = old | set([2,3,4])

cha = new - old

print(cha)