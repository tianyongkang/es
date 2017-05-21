import urllib2,urllib,sys
url = "http://ucw-pro.thinkjoy.com.cn/login"
info = [('userName','gbdai'),('password','xy@thinkjoy')]
getURL = urllib.urlencode(info)
request = urllib2.Request(getURL)
response = urllib2.urlopen(request)

print response.read()