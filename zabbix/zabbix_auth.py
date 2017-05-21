#!/usr/bin/python
#--*-- coding=utf8 --*--

import json
import urllib2

def zabbix_auth():
    #url = 'http://10.10.68.11/zabbix/api_jsonrpc.php'
    url = 'http://172.31.0.5/api_jsonrpc.php'
    header = {"Content-Type": "application/json-rpc"}
    value = {"jsonrpc":"2.0","method":"user.login","params": {"user": "Admin","password": "zabbix"},"id": 1}
    try:
        data = json.dumps(value)
        request = urllib2.Request(url, data)
        for key in header:
            request.add_header(key,header[key])

        print eval(urllib2.urlopen(request).read())["result"]
        #return '17ffc16bbd803845d79da0d13ebb94df'
    except (urllib2.URLError,urllib2.HTTPError, KeyError), e:
        print 'zabbix auth have an error:', e

zabbix_auth()
