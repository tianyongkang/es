import urllib2,urllib

url = urllib.urlopen('http://10.10.74.14:8082/mbean?objectname=java.lang%3Atype%3DOperatingSystem').read()
print url