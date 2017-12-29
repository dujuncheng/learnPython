# encoding=utf-8

# 保存cookie 在一个变量中

import urllib2
import cookielib

#声明一个CookieJar对象实例cookie, 来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handle = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handle)
#此处的open方法同urllib的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')

for item in cookie:
    print item
